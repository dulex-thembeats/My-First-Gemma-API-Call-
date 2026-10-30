MODEL=
"gemma-4-26b-a4b-it"
curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
-H "x-goog-api-key: $GEMINI
API
KEY" \
_
_
-H "Content-Type: application/json" \
-X POST \
-d '{"contents":[{"parts":[{"text":"Explain open source in 3 sentences.
"}]}]}'