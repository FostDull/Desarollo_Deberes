# Gemini.py
#pip install fastapi uvicorn python-multipart pandas google-generativeai
#pip install pandas
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import google.generativeai as genai

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir los archivos estáticos (index.html, etc.)
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# Tu cliente gemini
client = genai.Client(
    api_key="AIzaSyDJulUJdd1RZLvoBLds9bBvOvVDNMOHAx4"
)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_excel(contents)
    text_df = df.to_string()  # convertir a string para el prompt

    # Configuración que quieres pasar
    generation_config = {
        "temperature": 0.5,        
        "top_p": 0.9,             
        "top_k": 40,             
        "max_output_tokens": 1024 
    }

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"en base al párrafo '{text_df}', cuales son los 5 temas principales en las conversaciones en formato json",
        generation_config=generation_config
    )

    return JSONResponse(content={"result": response.text})
