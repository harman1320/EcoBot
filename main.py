from dotenv import load_dotenv
import os
from groq import Groq
from flask import Flask, render_template, jsonify, url_for, request

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
print("API_KEY", API_KEY)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods = ["POST"])
def ask():
    try:
        client = Groq(api_key=API_KEY)
        query = request.form.get('query')

        chat_completion = client.chat.completions.create(
        messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": query,
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_completion_tokens=1024
        )

        print(chat_completion.choices[0].message.content)

        data = chat_completion.choices[0].message.content

        return jsonify({"response": data}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)