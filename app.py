from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Usuario, Medicion # Importamos las clases del otro archivo
from datetime import datetime
import os 

# --- CONFIGURACIÓN DE LA APP ---
app = Flask(__name__)

# Configuración flexible de la base de datos
# Busca una URL de base de datos en las variables de entorno (para PostgreSQL en producción/local)
# Si no la encuentra, usa SQLite como respaldo (para desarrollo simple)
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cardiosense.db'
    print("ADVERTENCIA: No se encontró DATABASE_URL. Usando SQLite.")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'una_llave_secreta_de_respaldo')

# --- INICIALIZACIÓN DE LA BASE DE DATOS ---
db.init_app(app)

# --- RUTAS DE LA APLICACIÓN ---

@app.route('/')
def dashboard():
    # Renderiza la nueva página de bienvenida (landing hero)
    return render_template('index.html')

@app.route('/mediciones', methods=['GET', 'POST'])
def gestionar_mediciones():
    # Esta ruta maneja tanto la visualización (GET) como la creación (POST) de mediciones.
    
    if request.method == 'POST':
        # Lógica para AGREGAR una nueva medición
        user_id = request.form.get('user_id')
        sistolica = request.form.get('sistolica')
        diastolica = request.form.get('diastolica')

        # Validación simple
        if not user_id or not sistolica or not diastolica:
            flash('Todos los campos son obligatorios.', 'error')
        else:
            # Creamos la nueva medición
            nueva_medicion = Medicion(
                user_id=int(user_id),
                systolic_pressure=int(sistolica),
                diastolic_pressure=int(diastolica)
            )
            db.session.add(nueva_medicion)
            db.session.commit()
            flash('Medición guardada correctamente.', 'success')
        
        return redirect(url_for('gestionar_mediciones'))

    # Si el método es GET, mostramos la página con la lista de mediciones
    usuarios = Usuario.query.all()
    mediciones = Medicion.query.order_by(Medicion.measurement_timestamp.desc()).all()
    return render_template('mediciones.html', mediciones=mediciones, usuarios=usuarios)

@app.route('/mediciones/editar/<int:id>', methods=['GET', 'POST'])
def editar_medicion(id):
    medicion = Medicion.query.get_or_404(id)

    if request.method == 'POST':
        medicion.systolic_pressure = int(request.form['sistolica'])
        medicion.diastolic_pressure = int(request.form['diastolica'])
        db.session.commit()
        flash('Medición actualizada correctamente.', 'success')
        return redirect(url_for('gestionar_mediciones'))

    return render_template('editar_medicion.html', medicion=medicion)

@app.route('/mediciones/borrar/<int:id>', methods=['POST'])
def borrar_medicion(id):
    medicion = Medicion.query.get_or_404(id)
    db.session.delete(medicion)
    db.session.commit()
    flash('Medición eliminada correctamente.', 'success')
    return redirect(url_for('gestionar_mediciones'))


# --- FUNCIÓN PARA INICIALIZAR LA BASE DE DATOS ---
def setup_database(app):
    with app.app_context():
        db.create_all() # Crea todas las tablas definidas en models.py
        
        # Opcional: Crear un usuario de prueba si no existe
        if not Usuario.query.filter_by(user_id=1).first():
            usuario_prueba = Usuario(client_provided_id='MARIA_GARCIA_01')
            db.session.add(usuario_prueba)
            db.session.commit()
            print("Base de datos y usuario de prueba creados.")

# --- EJECUCIÓN DE LA APP ---
if __name__ == '__main__':
    setup_database(app) # Prepara la base de datos antes de correr
    app.run(debug=True)