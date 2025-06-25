# 🌐 Gemini API Backend + Frontend

Este proyecto es una aplicación web sencilla que expone un backend en **FastAPI** y un frontend en **HTML/JS** para analizar conversaciones en un archivo Excel usando la API de **Google Generative AI (Gemini)**.

## 🚀 Características
- Backend escrito en Python (FastAPI).
- Endpoint `/analyze` que recibe un archivo Excel (`.xlsx`), extrae su contenido y consulta a Gemini para devolver los 5 temas principales.
- Interfaz frontend sencilla en HTML y JS que permite subir un archivo y ver el resultado en pantalla.
- Configuración CORS para permitir peticiones desde el frontend.

---

## 🧑‍💻 Requisitos

- Python 3.11 o superior
- Pip y entorno virtual
- Una clave API válida para Google Generative AI (Gemini)

---

## 📂 Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/tu-usuario/gemini-fastapi.git
    cd gemini-fastapi
    ```

2. Crea y activa un entorno virtual:
    ```bash
    python -m venv venv
    source venv/Scripts/activate  # Windows
    source venv/bin/activate      # Linux/Mac
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Configura tu clave API en `Gemini.py`:
    ```python
    client = genai.Client(
        api_key="TU_API_KEY"
    )
    ```

---

## 🔧 Ejecución

1. Ejecuta el servidor:
    ```bash
    uvicorn Gemini:app --reload
    ```
2. Abre el frontend en `static/index.html` en tu navegador:
    ```
    http://127.0.0.1:8000/
    ```

---

## 📝 Endpoints

| Método | Endpoint | Descripción |
|--------|-----------|------------|
| `POST` | `/analyze` | Sube un Excel y recibe los 5 temas principales en JSON |

---

## 🧠 Tecnologías

- [FastAPI](https://fastapi.tiangolo.com/)
- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [Pandas](https://pandas.pydata.org/)
- HTML, CSS y JS (frontend simple)

---

## 📜 Licencia
Este proyecto se distribuye bajo la licencia MIT. ¡Siéntete libre de usarlo!

---

## 🤝 Contribuciones
Se aceptan pull requests y sugerencias. Para cambios mayores, por favor abre primero un issue para discutir qué te gustaría cambiar.

---

💡 ¡Espero que te sirva! Personalízalo con tu nombre, el enlace correcto al repo y cualquier detalle adicional que quieras incluir. ¿Quieres que también te prepare automáticamente un `requirements.txt` para que todo esté completo?
