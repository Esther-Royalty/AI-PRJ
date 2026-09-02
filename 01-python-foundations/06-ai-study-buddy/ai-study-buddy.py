import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


class StudyBuddy:
    def __init__(self, filename="quiz_history.json"):
        self.filename = filename
        self.history = self.load_history()

    def load_history(self):
     try:
        with open(self.filename, "r") as file:
           return json.load(file)
     except FileNotFoundError:
        return []

    def save_history(self):
       try: 
          with open(self.filename, "w") as file:
             save_history = json.dump(self.history, file)
       except Exception as e:
          print("An error occured while saving history:", e)

    def generate_quiz(self, notes):
       prompt = f"""You are a study assistant. Based on these notes, write 5 short quiz questions to test understanding. 
       Do not provide answers. Just the questions numbered 1 to 5. 
       Notes: {notes}"""

       response = client.models.generate_content(
          model="gemini-3.6-flash",
          contents=prompt
       )
       return response.text

    def add_to_history(self, notes, quiz):
       new_history = {"notes": notes, "quiz": quiz}
       self.history.append(new_history)


buddy = StudyBuddy()

print("AI Study Buddy: Paste your notes, get a quiz. Type 'stop' to exit.\n")

while True:
    notes = input("Paste your notes: ")

    if notes.lower() == "stop":
      break

    quiz = buddy.generate_quiz(notes)
    print("\n" + quiz + "\n")
    print(quiz)
    print()

    buddy.add_to_history(notes, quiz)

buddy.save_history()
print(f"Saved {len(buddy.history)} quiz sessions to {buddy.filename}. Bye!")
