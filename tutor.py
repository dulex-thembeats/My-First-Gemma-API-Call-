from google import genai
from google.genai import types

TUTOR = "Be a patient tutor. Use plain, short sentences."
config = types.GenerateContentConfig(system_instruction=TUTOR)

client = genai.Client()
response = client.models.generate_content(
    model="gemma-4-26b-a4b-it",
    config = types.GenerateContentConfig(
    system_instruction=TUTOR,
    thinking_config=types.ThinkingConfig(thinking_level="minimal")),
    contents="What is an API?",
)
print(response.text)
