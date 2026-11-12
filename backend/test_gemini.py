
from app.gemini_service import client, MODEL_NAME

print("Testing model:", MODEL_NAME)

response = client.models.generate_content(
    model=MODEL_NAME,
    contents="Reply with exactly: Gemini connection successful"
)

print("Gemini response:", response.text)
