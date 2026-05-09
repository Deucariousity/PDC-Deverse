import time
import os
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["POST"])
def disabled_worker():
    print("Worker is intentionally disabled. Message was received but not processed.")
    return "Worker disabled for failure simulation", 500

@app.route("/health", methods=["GET"])
def health():
    return "worker disabled but service is running", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    print("Worker intentionally disabled for fault injection test.")
    app.run(host="0.0.0.0", port=port)