from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Se inicializa db, pero se vinculará a la app de Flask más adelante
db = SQLAlchemy()

# Tabla de Unión para la relación muchos-a-muchos entre Predicciones y Recomendaciones
prediccion_recomendaciones = db.Table('prediccion_recomendaciones',
    db.Column('prediction_id', db.Integer, db.ForeignKey('predicciones.prediction_id'), primary_key=True),
    db.Column('recommendation_id', db.Integer, db.ForeignKey('recomendaciones.recommendation_id'), primary_key=True)
)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    user_id = db.Column(db.Integer, primary_key=True)
    client_provided_id = db.Column(db.String(255), unique=True, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones
    mediciones = db.relationship('Medicion', backref='usuario', lazy=True, cascade="all, delete-orphan")
    alertas = db.relationship('Alerta', backref='usuario', lazy=True, cascade="all, delete-orphan")

class Medicion(db.Model):
    __tablename__ = 'mediciones'
    measurement_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.user_id'), nullable=False)
    systolic_pressure = db.Column(db.Integer, nullable=False)
    diastolic_pressure = db.Column(db.Integer, nullable=False)
    measurement_timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Relación
    prediccion = db.relationship('Prediccion', backref='medicion', uselist=False, cascade="all, delete-orphan")

class Prediccion(db.Model):
    __tablename__ = 'predicciones'
    prediction_id = db.Column(db.Integer, primary_key=True)
    measurement_id = db.Column(db.Integer, db.ForeignKey('mediciones.measurement_id'), unique=True, nullable=False)
    risk_level = db.Column(db.String(100))
    risk_score = db.Column(db.Float)
    model_version = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relación muchos-a-muchos con Recomendaciones
    recomendaciones = db.relationship('Recomendacion', secondary=prediccion_recomendaciones, lazy='subquery',
        backref=db.backref('predicciones', lazy=True))

class Alerta(db.Model):
    __tablename__ = 'alertas'
    alert_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.user_id'), nullable=False)
    alert_type = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Recomendacion(db.Model):
    __tablename__ = 'recomendaciones'
    recommendation_id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100))
    text = db.Column(db.Text, nullable=False)