from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = "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"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    message = request.json.get("message")
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": message}]
    )
    if completion.choices[0].message != None:
        return completion.choices[0].message
    else:
        return 'Failed to get a response'


if __name__ == "__main__":
    app.run()
