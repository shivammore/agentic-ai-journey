import os, httpx
from dotenv import load_dotenv

load_dotenv()
resp = httpx.post(
    "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
    headers={"Authorization": f"Bearer {os.getenv('GEMINI_API_KEY')}"},
    json={
        "model": "gemini-2.5-flash",
        "messages": [
            {"role": "system", "content": "You are a helpful tutor."},
            {"role": "user", "content": "Explain an AI agent in 2 lines."},
        ],
    },
    timeout=60,
)
data = resp.json()
print(data["choices"][0]["message"]["content"])
print("Tokens used:", data["usage"])