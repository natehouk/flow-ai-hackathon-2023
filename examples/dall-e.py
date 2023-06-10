curl https://api.openai.com/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "prompt": "A photo of a trader staring at a Bloomberg terminal sweating and with his head in his hands.",
    "n":1,
    "size":"1024x1024"
   }'