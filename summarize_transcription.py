import ollama

SUMMARIZE_CLASS_VIDEO_NOTES_PROMPT = """
You are a helpful assistant that summarizes class video notes.

The notes should be concise and to the point, without missing any important information. Only include information from the transcription. The notes can be in this format:
<Heading>
<Subheading 1>
- Point 1
- Point 2
- Point 3
</Subheading 1>
<Subheading 2>
- Point 1
- Point 2
- Point 3
</Subheading 2>
</Heading>
Summary:
<Summary>
Summary of the notes.
</Summary>

Following the formatting rules:
    1. Don't write out the tags <Heading>, <Subheading 1>, <Subheading 2>, <Summary>, etc. Just write the content.
    2. Don't output anything between the thinking tags <think> and </think>.

Here is the transcription:
{transcription}
"""

def run_inference(transcription, prompt, model="deepseek-r1:8b"):
    response = ollama.chat(
        model=model,
        messages=[
            {"role": "user", "content": prompt.format(transcription=transcription)}
        ]
    )
    return response['message']['content']

