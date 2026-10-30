from google import genai
client = genai.Client()
for m in client.models.list():
    if "gemma" in m.name:
        print(m.name)