from flask import Flask, request, render_template, jsonify
from google import genai

client=genai.Client(api_key="GEMINI_API_KEY")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/chat",methods=["POST"])
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
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return jsonify({"reply": response.text})
app.run(port=8000)
