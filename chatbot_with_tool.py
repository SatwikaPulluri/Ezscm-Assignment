import os
import json
import re
from dotenv import load_dotenv
import google.generativeai as genai
import calculator_tool as calc

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found! Please add it to .env file.")

# Configure Gemini client
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

LOG_FILE = "logs_level2.json"

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

def clean_output(text: str) -> str:
    """Remove markdown/bullets for clean CLI output"""
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    text = re.sub(r"^[\*\-•]\s*", "", text, flags=re.MULTILINE)
    return text.strip()

def detect_math(query: str):
    """Detect simple math like '15 + 23'"""
    import re
    match = re.match(r"^\s*(\d+)\s*([\+\-\*/])\s*(\d+)\s*$", query)
    if match:
        a, op, b = match.groups()
        a, b = int(a), int(b)
        if op == "+": return calc.add(a, b)
        if op == "-": return calc.subtract(a, b)
        if op == "*": return calc.multiply(a, b)
        if op == "/": return calc.divide(a, b)
    return None

def ask_llm(question):
    # First check if it's a math query
    result = detect_math(question)
    if result is not None:
        return f"The result is: {result}"

    # Otherwise use LLM
    prompt = f"""
    You are a helpful assistant.
    Answer clearly and step by step.
    Format your response ONLY as a numbered list (1., 2., 3., ...).
    Keep each point short and concise.
    Do NOT use bullet points or markdown formatting.
    Question: {question}
    """
    response = model.generate_content(prompt)
    return clean_output(response.text)

def main():
    print("🤖 LLM + Calculator Smart Assistant (Level 2)")
    print("Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye 👋")
            break
        response = ask_llm(user_input)
        print("Assistant:\n" + response)
        save_log(user_input, response)

if __name__ == "__main__":
    main()
