import streamlit as st
import whisper
import os
import requests
import json

# Load the Whisper model
@st.cache_resource
def load_whisper_model():
    return whisper.load_model("small.en")

model = load_whisper_model()

def summarize_with_ollama(text):
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": "llama3.1:8b",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that summarizes text."},
            {"role": "user", "content": f"Summarize the following text:\n\n{text}"}
        ],
        "stream": False
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return json.loads(response.text)['message']['content']
    else:
        return f"Error: Unable to generate summary. Status code: {response.status_code}"

st.title("Community Call Transcription and Summarization")

uploaded_file = st.file_uploader("Choose an audio file", type=['mp3', 'wav'])

if uploaded_file is not None:
    # Create the uploads directory if it doesn't exist
    os.makedirs("uploads", exist_ok=True)
    
    # Save the uploaded file
    filepath = os.path.join("uploads", uploaded_file.name)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    with st.spinner("Transcribing audio..."):
        results = model.transcribe(filepath)
        transcription = results['text']
    
    with st.spinner("Generating summary..."):
        summary = summarize_with_ollama(transcription)
    
    st.subheader("Transcription")
    st.write(transcription)
    
    st.subheader("Summary")
    st.write(summary)
