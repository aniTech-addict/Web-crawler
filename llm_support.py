from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY=os.getenv("GEMINI_API")

client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)