from google import genai
from google.genai import types

MODEL = "gemma-4-26b-a4b-it"
client = genai.Client()
fast = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_level="minimal"))

# 1. Conversation: the chat remembers earlier messages
chat = client.chats.create(model=MODEL, config=fast);
print(chat.send_message("Hi! I am Amina.").text)
print(chat.send_message("What is my name?").text)

# 2. Images: send a picture together with a question
img = client.files.upload(file="photo.jpg")
r = client.models.generate_content(
    model=MODEL,
    config=fast,
    contents=[img, "Write alt text for this image."],
)
print(r.text)

# 3. Thinking: slower, more careful reasoning
cfg = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_level="minimal")
)
r = client.models.generate_content(
    model=MODEL,
    config=cfg,
    contents="A farmer has 17 goats. All but 9 run away. How many are left?",
)
print(r.text)
