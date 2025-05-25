# Whisper Summary

A web application for transcribing and summarizing audio files using OpenAI's Whisper model.

## Features

- Upload audio files (MP3, WAV, M4A, FLAC)
- Transcribe audio to text using Whisper
- Generate customized summaries based on user prompts
- Modern, responsive user interface
- Drag-and-drop file upload

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/whisper-summary.git
   cd whisper-summary
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python main.py
   ```

5. Open your browser and navigate to `http://localhost:8000`

## API Endpoints

- `GET /`: Web interface for audio transcription
- `GET /api`: API information
- `POST /transcribe/`: Endpoint for audio transcription and summarization

## License

See the LICENSE file for details.
