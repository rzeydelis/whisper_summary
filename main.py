from fastapi import FastAPI, File, UploadFile
from transcribe_audio import transcribe_audio_file
import tempfile
import os
import uvicorn

app = FastAPI(title="Audio Transcription API")

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Audio Transcription API",
        "endpoints": {
            "transcribe": "/transcribe/ (POST) - Upload an audio file for transcription"
        },
        "documentation": "/docs - Interactive API documentation"
    }

@app.post("/transcribe/")
async def transcribe_endpoint(file: UploadFile = File(...)):
    # Save the uploaded file temporarily
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    try:
        contents = await file.read()
        with open(temp_file.name, 'wb') as f:
            f.write(contents)
        
        # Transcribe the audio file
        result = transcribe_audio_file(temp_file.name, model_name="turbo")
        return {"filename": file.filename, "transcription": result}
    finally:
        # Clean up the temp file
        temp_file.close()
        os.unlink(temp_file.name)


def run_transcribe_audio_file(audio_file_path, model_name="turbo"):
    return transcribe_audio_file(audio_file_path, model_name)

if __name__ == "__main__":
    uvicorn.run("src.main:app", port=8000, reload=True, host="0.0.0.0")
