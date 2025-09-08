import os
import json
import re
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found! Please add it to .env file.")

# Configure Gemini client
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

LOG_FILE = "logs_level1.json"

def save_log(user_input, response):
    log_entry = {"user": user_input, "assistant": response}
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump([log_entry], f, indent=4)
    else:
        with open(LOG_FILE, "r+", encoding="utf-8") as f:
            data = json.load(f)
            data.append(log_entry)
            f.seek(0)
            json.dump(data, f, indent=4)

def clean_markdown(text: str) -> str:
    """Remove Markdown-style bold/italic for clean CLI output"""
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)  # **bold** → bold
    text = re.sub(r"\*(.*?)\*", r"\1", text)      # *italic* → italic
    return text

def ask_llm(question):
    # If math is detected → refuse
    if any(op in question.lower() for op in ["+", "-", "times", "multiply", "add", "sum"]):
        return "I cannot do calculations. Please use a calculator tool."

    prompt = f"""
    You are a helpful assistant.
    Always explain step by step and structure output clearly with numbered points.
    Avoid using bold or italic Markdown formatting.
    Question: {question}
    """

    response = model.generate_content(prompt)
    return clean_markdown(response.text)

def main():
    print("🤖 LLM Smart Assistant (Level 1) [Gemini]")
    print("Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye 👋")
            break
        response = ask_llm(user_input)
        print("Assistant:", response)
        save_log(user_input, response)

if __name__ == "__main__":
    main()
