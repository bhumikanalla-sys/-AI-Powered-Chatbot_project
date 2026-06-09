from flask import Flask, render_template, request
from chatbot import get_response
from database import create_db, save_chat

app = Flask(__name__)

create_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def chatbot_response():
    user_text = request.args.get("msg")

    bot_reply = get_response(user_text)

    save_chat(user_text, bot_reply)

    return bot_reply

if __name__ == "__main__":
    app.run(debug=True)