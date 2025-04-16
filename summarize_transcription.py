import ollama

def load_chat_model(self, content, model="deepseek-r1"):
    response = ollama.chat(
        model=model,
        messages=[
            {"role": "user", "content": content}
        ]
    )
    return response['message']['content']


