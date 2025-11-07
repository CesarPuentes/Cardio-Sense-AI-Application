# ❤️ CardioSense AI

CardioSense AI es una aplicación web desarrollada con **Flask** para monitorear la salud cardiovascular. Permite a los usuarios registrar mediciones de presión arterial y está diseñada para ofrecer análisis de riesgo impulsados por IA y recomendaciones personalizadas.

---

## 🚀 Cómo Empezar

Sigue estos pasos para ejecutar el proyecto en tu máquina local.

### Prerrequisitos

* Python 3.8+
* pip
* Docker (para pruebas con PostgreSQL)

### Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone <la-url-de-tu-repositorio>
    cd CardioSenseAI
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # Para Windows
    py -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instala las dependencias requeridas:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta la aplicación (con SQLite):**
    Para un inicio rápido, puedes usar la base de datos SQLite por defecto.
    ```bash
    python app.py
    ```
    La aplicación estará disponible en `http://127.0.0.1:5000`.

---

### 🐘 Pruebas con PostgreSQL (Local)

Para simular el entorno de producción, puedes ejecutar la aplicación conectada a una base de datos PostgreSQL usando Docker.

1.  **Inicia un contenedor de PostgreSQL:**
    ```bash
    # Reemplaza 'tu_clave_segura' con una contraseña sin caracteres especiales (@, #, $)
    docker run --name local-postgres -e POSTGRES_PASSWORD=tu_clave_segura -p 5432:5432 -d postgres
    ```

2.  **Crea la base de datos dentro del contenedor:**
    ```bash
    # Conéctate al contenedor
    docker exec -it local-postgres psql -U postgres

    # Una vez dentro, ejecuta el comando SQL para crear la base de datos y sal
    CREATE DATABASE cardiosense_local;
    \q
    ```

3.  **Ejecuta la aplicación conectada a PostgreSQL:**
    Define la variable de entorno `DATABASE_URL` antes de iniciar la app.
    ```bash
    # Reemplaza 'tu_clave_segura' con la misma contraseña del paso 1
    export DATABASE_URL="postgresql://postgres:tu_clave_segura@localhost:5432/cardiosense_local"
    python app.py
    ```

---

## 🐳 Ejecución con Docker

También puedes ejecutar la aplicación completa dentro de un contenedor Docker.

1.  **Construye la imagen de Docker:**
    ```bash
    docker build -t cardiosense-flask .
    ```

2.  **Ejecuta el contenedor:**
    ```bash
    docker run -d -p 8080:8080 --name cardiosense-app cardiosense-flask
    ```
    La aplicación estará disponible en `http://localhost:8080`.

---

## 📸 Vista Previa de la Aplicación

Aquí tienes una demostración rápida de las funcionalidades principales de la aplicación.

![Demostración de CardioSense AI](./sample.png)

---

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python, Flask
* **ORM de Base de Datos:** Flask-SQLAlchemy
* **Motor de Base de Datos:** PostgreSQL / SQLite
* **Frontend:** HTML, CSS, Jinja2