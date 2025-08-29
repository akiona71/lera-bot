import os
import openai

# Ключ берём из переменной окружения
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_lera(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Ошибка: {e}"

if __name__ == "__main__":
    while True:
        user_input = input("Ты: ")
        if user_input.lower() in ["выход", "exit", "quit"]:
            break
        print("Лера:", ask_lera(user_input))
