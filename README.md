# 📚 Study Chatbot — LearnLoop

A lightweight AI-powered Physics and Chemistry tutor chatbot built with Flask and Google Gemini 2.5 Flash. Ask questions and get concise, conversational explanations — no textbook jargon.

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![Gemini](https://img.shields.io/badge/Google%20Gemini-2.5%20Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)

---

## ✨ Features

- **🧪 Physics & Chemistry Focus** — Tutor specialized in Physics and Chemistry topics
- **💬 Conversational Tone** — Short, simple answers (3–5 lines) without textbook-style paragraphs
- **⚡ Powered by Gemini** — Uses Google Gemini 2.5 Flash for fast, accurate responses
- **🌐 Web Interface** — Clean chat UI served via Flask templates
- **🔌 REST API** — Simple `/chat` endpoint for integration with other apps

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python, Flask |
| **AI Model** | Google Gemini 2.5 Flash |
| **Frontend** | HTML, CSS, JavaScript (Jinja2 templates) |

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.9+** installed
- A **Google Gemini API Key** ([Get one here](https://aistudio.google.com/apikey))

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/sujitha-kotyada/study-chatbot.git
   cd study-chatbot
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**

   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**

   ```bash
   pip install flask google-genai
   ```

5. **Configure your API key**

   Create a `.env` file in the project root:

   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

   > ⚠️ **Important**: Never hardcode API keys in source code. Use environment variables.

6. **Run the application**

   ```bash
   python main.py
   ```

7. **Open in browser**

   Navigate to [http://localhost:5000](http://localhost:5000)

---

## 📖 Usage

1. Open the chat interface in your browser
2. Type a Physics or Chemistry question
3. Get a concise, conversational answer in seconds

### Example Questions
- "What is Newton's third law?"
- "Explain covalent bonding"
- "Why does ice float on water?"
- "What is the difference between speed and velocity?"

---

## 🔌 API Reference

### `POST /chat`

Send a message and receive an AI response.

**Request:** `application/json`

```json
{
  "message": "What is Ohm's law?"
}
```

**Response:** `application/json`

```json
{
  "reply": "Ohm's law states that the current flowing through a conductor is directly proportional to the voltage across it, given constant temperature. The formula is V = IR, where V is voltage, I is current, and R is resistance."
}
```

---

## 📁 Project Structure

```
study-chatbot/
├── main.py              # Flask backend with Gemini AI integration
├── templates/
│   └── index.html       # Chat UI frontend
└── README.md
```


## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙋‍♀️ Author

**Sujitha Kotyada** — [@sujitha-kotyada](https://github.com/sujitha-kotyada)
