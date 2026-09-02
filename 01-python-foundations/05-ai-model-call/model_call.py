import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

print("AI Prompt Tool - type 'stop' to exit\n")

while True:
    user_prompt = input("Ask me anything: ")

    if user_prompt.lower() == "stop":
        print("Goodbye!")
        break

    full_prompt = f"You are a helpful cooking assistant. Only answer questions about food and recipes. User question: {user_prompt}"
    
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=full_prompt
    )

    print("\n" + response.text + "\n")