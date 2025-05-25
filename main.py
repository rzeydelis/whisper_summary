from fastapi import FastAPI, File, UploadFile, Form
from transcribe_audio import transcribe_audio_file
from summarize_transcription import run_inference
import tempfile
import os
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI(title="Audio Transcription API")

# Set up templates directory
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "src" / "front_end_templates"))

# Mount static files directory if needed
# app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

@app.get("/", response_class=HTMLResponse)
async def home():
    # Return the home.html template
    return templates.TemplateResponse("home.html", {"request": {}})

@app.get("/api")
def read_root():
    return {
        "message": "Welcome to the Audio Transcription API",
        "endpoints": {
            "transcribe": "/transcribe/ (POST) - Upload an audio file for transcription"
        },
        "documentation": "/docs - Interactive API documentation"
    }

@app.post("/transcribe/")
async def transcribe_endpoint(file: UploadFile = File(...), user_prompt: str = Form(...)):
    # Save the uploaded file temporarily
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    try:
        contents = await file.read()
        with open(temp_file.name, 'wb') as f:
            f.write(contents)
        
        # Transcribe the audio file
        transcription = transcribe_audio_file(temp_file.name, model_name="turbo")
        summary = run_inference(transcription, user_prompt)
        return {"filename": file.filename, "transcription": transcription, "summary": summary}
    except Exception as e:
        return {"Received error while transcribing audio file": str(e)}
    finally:
        # Clean up the temp file
        temp_file.close()
        os.unlink(temp_file.name)

def run_transcribe_audio_file(audio_file_path, model_name="turbo"):
    return transcribe_audio_file(audio_file_path, model_name)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True, host="127.0.0.1")
