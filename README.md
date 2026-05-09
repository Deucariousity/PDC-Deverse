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



Demo Video Link

Add your demo video or GIF link here.



Group Members

Member 1 - Baclayo, Myka Angelie

Member 2 - Dinorog, Artjohn Clark Dinorog

Member 3 - Oplimo, Kent

Member 4 - Seromines, Ralph Joshua



Individual Reflections

Member 1 - Baclayo, Myka Angelie

Write your reflection here.

Member 2 - Dinorog, Artjohn Clark Dinorog

Write your reflection here.

Member 3 - Oplimo, Kent

Write your reflection here.

Member 4 - Seromines, Ralph Joshua

Write your reflection here.



Conclusion
The distributed voting system successfully demonstrated event-driven communication, asynchronous processing, fault tolerance, and persistent storage using Google Cloud Platform.
