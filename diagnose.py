import google.genai
from google import genai
from google.genai import types

print("SDK version:", google.genai.__version__)
client = genai.Client()

minimal = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_level="minimal"))

tests = [
    ("gemma-4-26b-a4b-it", None, "default"),
    ("gemma-4-26b-a4b-it", minimal, "thinking off"),
    ("gemma-4-31b-it", None, "default"),
]
gemini = [m.name.split("/")[-1] for m in client.models.list()
          if "gemini" in m.name and "flash" in m.name]
if gemini:
    tests.append((gemini[0], None, "default (Gemini, for comparison)"))

for model, cfg, label in tests:
    try:
        r = client.models.generate_content(
            model=model, contents="Say hello in one sentence.", config=cfg)
        print("OK  ", model, "|", label, "->", r.text.strip()[:60])
    except Exception as e:
        print("FAIL", model, "|", label, "->", str(e)[:90])