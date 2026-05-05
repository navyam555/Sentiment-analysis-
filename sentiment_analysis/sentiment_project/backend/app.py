from flask import Flask, request, jsonify
from sentiment import get_sentiment
from reasoning import get_issue
from intent import get_intent
from db import save_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.json["review"]

    sentiment = get_sentiment(text)
    issue = get_issue(text)
    intent = get_intent(text)

    data = {
        "review": text,
        "sentiment": sentiment,
        "issue": issue,
        "intent": intent
    }

    save_data(data)
    data["_id"] = str(data.get("_id", ""))

    return jsonify(data)

app.run(debug=True)