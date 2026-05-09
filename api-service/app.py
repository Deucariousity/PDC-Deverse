from flask import Flask, request
from google.cloud import pubsub_v1
import json
import os

app = Flask(__name__)

project_id = "cs323-voting-system-deverse"
topic_id = "vote-topic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

@app.route("/vote", methods=["POST"])
def receive_vote():
    vote = request.get_json()

    if not vote:
        return {"error": "Invalid payload"}, 400

    required_fields = ["user_id", "poll_id", "choice", "timestamp"]

    for field in required_fields:
        if field not in vote:
            return {"error": f"Missing {field}"}, 400

    try:
        data = json.dumps(vote).encode("utf-8")

        publisher.publish(topic_path, data)

        return {"status": "accepted"}, 200

    except Exception as e:
        return {"error": str(e)}, 500

@app.route("/")
def home():
    return "Voting API Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))