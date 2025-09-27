# ❤️ CardioSense AI

CardioSense AI es una aplicación web desarrollada con **Flask** para monitorear la salud cardiovascular. Permite a los usuarios registrar mediciones de presión arterial y está diseñada para ofrecer análisis de riesgo impulsados por IA y recomendaciones personalizadas.

---

## 🚀 Cómo Empezar

Sigue estos pasos para ejecutar el proyecto en tu máquina local.

### Prerrequisitos

* Python 3.8+
* pip

### Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone <la-url-de-tu-repositorio>
    cd CardioSenseAI
    ```

2.  **Crea y activa un entorno virtual (recomendado):**
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

4.  **Ejecuta la aplicación:**
    ```bash
    python app.py
    ```
    La aplicación estará disponible en `http://127.0.0.1:5000`.

---

## 📸 Vista Previa de la Aplicación

Aquí tienes una demostración rápida de las funcionalidades principales de la aplicación.

![Demostración de CardioSense AI](./Sample.gif)

---

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python, Flask
* **ORM de Base de Datos:** Flask-SQLAlchemy
* **Motor de Base de Datos:** SQLite
* **Frontend:** HTML, CSS, Jinja2