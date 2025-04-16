import whisper
from pathlib import Path
from typing import Optional


def transcribe_audio_file(audio_path: str, model_name: str) -> Optional[str]:
    """
    Transcribe an audio file using OpenAI's Whisper model.

    Args:
        audio_path (str): Path to the audio file to transcribe
        model_name (str): Name of the Whisper model to use (e.g., 'tiny', 'base', 'small', 'medium', 'large')

    Returns:
        Optional[str]: Transcribed text if successful, None if transcription fails

    Raises:
        FileNotFoundError: If the audio file does not exist
        ValueError: If the model name is invalid
    """
    try:
        audio_file = Path(audio_path)
        if not audio_file.exists():
            raise FileNotFoundError(f"Audio file not found: {audio_path}")

        model = whisper.load_model(model_name)
        result = model.transcribe(
            str(audio_file),
            task="transcribe",
        )
        return result["text"]
    except Exception as e:
        print(f"Error during transcription: {str(e)}")
        return None