import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Lera bot is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    # Заглушка — тут можно подключить OpenAI или твою логику бота
    reply = f"Ты написал: {user_message}"
    return jsonify({"reply": reply})
