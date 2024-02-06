from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = ""


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    try:
        message = request.json.get("message")
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}]
        )
        if completion.choices[0].message is not None:
            return completion.choices[0].message
        else:
            return 'Failed to get a response'
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(debug=True)
