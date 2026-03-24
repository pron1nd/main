from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/")
async def read_index():
    # Указываем путь к файлу
    file_path = "public/index.html"
    return FileResponse(file_path)