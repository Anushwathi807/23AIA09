from flask import Flask, jsonify, request
import requests
import _heapq
from datetime import datetime

app = Flask(__name__)
NOTIFICATIONS_API = "http://4.224.186.213/evaluation-service/notifications"
AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJhbnVzaHdhdGhpcmFuZ2FuYXRoYW5AZ21haWwuY29tIiwiZXhwIjoxNzgyODA0ODgwLCJpYXQiOjE3ODI4MDM5ODAsImlzcyI6IkFmZm9yZCBNZWRpY2FsIFRlY2hub2xvZ2llcyBQcml2YXRlIExpbWl0ZWQiLCJqdGkiOiIzZjQ2NWNiNy1kZjU0LTRkY2MtODBkMC0wY2E0ODQzMGVkYzEiLCJsb2NhbGUiOiJlbi1JTiIsIm5hbWUiOiJhbnVzaHdhdGhpIHIiLCJzdWIiOiJhMWVjOTgyZi1kZjg5LTQ0OWUtYWUyOS0wMDhhNmM4NmU1ZjMifSwiZW1haWwiOiJhbnVzaHdhdGhpcmFuZ2FuYXRoYW5AZ21haWwuY29tIiwibmFtZSI6ImFudXNod2F0aGkgciIsInJvbGxObyI6IjIzYWlhMDkiLCJhY2Nlc3NDb2RlIjoiV2pOeUNUIiwiY2xpZW50SUQiOiJhMWVjOTgyZi1kZjg5LTQ0OWUtYWUyOS0wMDhhNmM4NmU1ZjMiLCJjbGllbnRTZWNyZXQiOiJ0RHd1dkZhU1JXUFVtaHNOIn0.ckMmetca75hQh8l2wMbUJ-6Ot1MIb8UP_coLgHz1lC4"

WEIGHT = {"Placement": 3, "RESULT":2, "EVENT":1}

def fetch_notifications():
    headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}
    resp = requests.get(NOTIFICATIONS_API, headers=headers)
    resp.raise_for_status()
    return resp.json().get("notifications", [])

def score(notification):
    weight = WEIGHT.get(notification["Type"], 0)
    ts = datetime.strptime(notification["Timestamp"], "%Y-%m%d %H:%M:%S")
    return(weight, ts.timestamp())

@app.route("/priority-inbox", methods=['GET'])
def priority_inbox():
    n = int(requests.args.get("n", 10))
    notifications = fetch_notifications()
    top_n = sorted(notifications, key=score, reverse=True)[:n]
    return jsonify({"count": len(top_n), "notifications": top_n})
