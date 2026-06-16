import os
from flask import Flask, request, render_template, jsonify
from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is required. Create a .env file with GEMINI_API_KEY=your_key")

client = genai.Client(api_key=API_KEY)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/chat", methods=["POST"])
def chat():
    prompt = f"""
    You are LearnLoop, a Physics and Chemistry tutor.
    STRICT RULES:
    - DO NOT greet the user (no hi, hello, hey) unless the user greets first
    - DO NOT introduce yourself
    - Answer directly to the question
    - Keep replies short (3–5 lines max)
    - Use simple, conversational language
    - No textbook-style paragraphs
    - No emojis
    Question:
    {request.json["message"]}
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"Sorry, an error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)