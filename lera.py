import os
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Берём API-ключ из переменных окружения (Vercel → Settings → Environment Variables)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "✅ Lera-bot is running!"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"error": "message is required"}), 400

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )

        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # локальный запуск
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
