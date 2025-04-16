import ollama

def summarize_transcription(content, model="deepseek-r1"):
    response = ollama.chat(
        model=model,
        messages=[
            {"role": "user", "content": content}
        ]
    )
    return response['message']['content']

