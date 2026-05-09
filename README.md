# CS3A Deverse
PDC-Distributed Voting System on Google Cloud Platform

Project Overview
This project implements a fault-tolerant distributed voting system using Google Cloud Platform (GCP). Multiple edge nodes generate vote data and send it to a cloud-based API. The API publishes messages to Pub/Sub, a worker service processes the messages asynchronously, and Cloud Firestore stores the final vote records.

Architecture Diagram
Edge Nodes (edge.py)
        ↓
Cloud Run API (voting-api)
        ↓
Pub/Sub
  - vote-topic
  - vote-sub
        ↓
Cloud Run Worker (voting-worker)
        ↓
Firestore Database (deverse)
        ↓
votes Collection


Technologies Used
Python 3.11
Flask
Google Cloud Run
Google Cloud Pub/Sub
Google Cloud Firestore

Repository Structure

pdc-second-lab/
├── api-service/
├── worker-service/
├── edge-node/
├── distributed_voting_architecture.png
└── README.md

GCP Setup
Create project: `cs323-voting-system-deverse`
Enable:
Cloud Run Admin API
Cloud Pub/Sub API
Cloud Firestore API
Create Firestore database:
Native Mode
Region: `asia-southeast1`
Database ID: `deverse`
Create Pub/Sub:
Topic: `vote-topic`
Subscription: `vote-sub`
Deployment Instructions

Deploy API
```
cd api-service
gcloud run deploy voting-api --source . --region asia-southeast1 --allow-unauthenticated
```

Deploy Worker
```
cd worker-service
gcloud run deploy voting-worker --source . --region asia-southeast1 --no-allow-unauthenticated
```

Running Edge Nodes
Update `edge.py`:
```python
API_URL = "https://voting-api-110300713239.asia-southeast1.run.app/vote"
```
Run:
```
python edge-node/edge.py
```

Fault Injection
Duplicate Messages
Send the same vote multiple times.
Worker Failure
Temporarily disable the worker and observe:
API still accepts requests
Pub/Sub buffers messages
Firestore stops updating
Recovery
Restore the worker and observe queued messages being processed.
Performance Evaluation
End-to-end latency
Throughput
Eventual consistency
Automatic recovery
Cloud Run API Endpoint
Replace with your deployed URL:
`https://https:/voting-api-110300713239.asia-southeast1.run.app/vote`



> Demo Video Link

Add your demo video or GIF link here.



> Group Members

Member 1 - Baclayo, Myka Angelie

Member 2 - Dinorog, Artjohn Clark Dinorog

Member 3 - Oplimo, Kent

Member 4 - Seromines, Ralph Joshua



> Individual Reflections

Member 1 - Baclayo, Myka Angelie

Before this activity, i understood distributed systems mostly in theory. Building one on gcp made the concepts more concrete, though it came with a fair share of confusion along the way.

Setting up the cloud environment took longer than expected. Configuring pub/sub, firestore, and cloud run required a lot of attention to detail, and small mistakes caused issues that were not always easy to trace.
Running the edge node script was straightforward once everything was connected. What stood out was how independently each node operated, which reflects how real distributed clients behave.

The fault injection part was the most informative. When the worker was disabled, the api kept accepting requests and pub/sub continued buffering messages. When the worker was restored, it processed everything automatically. That showed me what fault tolerance actually looks like in practice.

Idempotency was something i underestimated at first. After seeing duplicate votes appear during the simulation, it became clear why a composite document id in firestore matters. Without it, duplicates would silently corrupt the data.The activity gave me a clearer picture of how distributed systems handle failure. A system does not need to be perfect to be reliable.

Member 2 - Dinorog, Artjohn Clark Dinorog

Working on this laboratory activity gave me a much better understanding of how distributed systems work in real life. At first, setting up Google Cloud services like Cloud Run, Pub/Sub, and Firestore was challenging, and I encountered several errors during deployment and configuration. However, as I connected each component and saw the votes move from the edge nodes to the API, through Pub/Sub, and finally into Firestore, the overall architecture became much clearer. What impressed me most was how the system continued to accept votes even when the worker service was disabled, and how everything recovered automatically once the worker was restored. This showed me how distributed systems are designed to handle failures without losing data. I also learned how techniques like retries and idempotency help keep the system reliable and consistent. Overall, this project was both challenging and rewarding, and it gave me practical experience and confidence in building scalable and fault-tolerant applications in the cloud.

Member 3 - Oplimo, Kent

 This project helped me better understand the distributed systems and cloud computing using Google Cloud Platform. I learned how different services like Cloud Run, Pub/Sub, and Firestore work together to create a reliable and fault-tolerant voting system. The project also showed the importance of asynchronous processing and message buffering during failures. Through deployment and fault injection testing, I gained practical experience in building scalable systems that can recover automatically and continue operating efficiently even when some components fail.

Member 4 - Seromines, Ralph Joshua

Write your reflection here.

This project helped me understand how distributed systems work in real-world environments using Google Cloud Platform. The system was divided into three services—API, Worker, and Edge Nodes—to improve scalability, resilience, and maintainability. Using Cloud Run, Pub/Sub, and Firestore allowed us to focus more on the system logic instead of managing infrastructure.

One of the biggest lessons was learning how asynchronous communication improves reliability. Instead of directly writing votes to the database, the API sends messages through Pub/Sub, allowing the system to continue accepting requests even if the worker service is delayed or temporarily unavailable.

We also encountered challenges such as duplicate messages because Pub/Sub uses “at-least-once” delivery. To solve this, we implemented idempotent processing in the worker so repeated messages would not affect the final results. Testing failures like disabling services or simulating network issues also showed how fault tolerance works in practice.

This project demonstrated important distributed systems concepts such as scalability, eventual consistency, asynchronous processing, and fault tolerance. It also taught me that collaboration and careful testing are very important because even small changes can affect multiple services across the system.

Overall, this project gave me practical experience in building cloud-based distributed applications and helped me better understand how modern scalable systems are designed and maintained.



> Conclusion:
The distributed voting system successfully demonstrated event-driven communication, asynchronous processing, fault tolerance, and persistent storage using Google Cloud Platform.
