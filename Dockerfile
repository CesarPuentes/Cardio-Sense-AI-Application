# Usa una imagen base oficial de Python (actualizada)
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos e instala las dependencias
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de tu aplicación al contenedor
COPY . .

# Expone el puerto que usará la aplicación
EXPOSE 8080

# Comando para ejecutar la aplicación con un servidor de producción como Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]