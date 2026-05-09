import requests
import uuid
import random
import time

API_URL = "https://voting-api-110300713239.asia-southeast1.run.app/vote"

EDGE_ID = random.randint(1, 100)

def generate_vote():
    return {
        "edge_id": EDGE_ID,
        "user_id": str(uuid.uuid4()),
        "poll_id": "poll_1",
        "choice": random.choice(["A", "B", "C"]),
        "timestamp": time.time()
    }

def send_vote(vote):
    retries = 3

    for attempt in range(retries):
        try:
            response = requests.post(API_URL, json=vote)

            print("Vote sent:", response.status_code)

            return

        except Exception as e:
            print("Transmission failed:", e)

            time.sleep(2)

def run_edge_node():
    while True:
        vote = generate_vote()

        print(f"Generated vote: {vote['user_id']}")

        send_vote(vote)

        time.sleep(random.uniform(1, 3))

run_edge_node()