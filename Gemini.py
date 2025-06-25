# Gemini.py
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import google.generativeai as genai

app = FastAPI()

# Configuración CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    # Agrega otros orígenes si es necesario
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Cambia a ["*"] para permitir todos (solo dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

genai.configure(
    api_key="AIzaSyDJulUJdd1RZvoBLds9bBvOvVDNMOHAx4"
)

# Montar carpeta estática en /static
app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.post("/analyze")
async def analyze(file: UploadFile = File(...), prompt: str = Form(...)):
    contents = await file.read()
    df = pd.read_excel(contents)

    # Tomar solo 100 filas si es muy grande
    if len(df) > 100:
        df = df.sample(n=100, random_state=42)

    text_df = df.to_string(index=False)

    generation_config = {
        "temperature": 0.5,
        "top_p": 0.9,
        "top_k": 40,
        "max_output_tokens": 1024
    }

    full_prompt = f"{prompt}. Aquí tienes el texto:\n{text_df}"
    response = genai.generate_content(
        model="gemini-1.5-flash",
        contents=full_prompt,
        generation_config=generation_config
    )

    return JSONResponse(content={"result": response.text})
