import whisper

def transcribe_audio_file(audio_path, model_name):
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path)
    return result["text"]