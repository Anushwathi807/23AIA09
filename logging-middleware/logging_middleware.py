import requests

LOG_API_URL = "http://4.224.186.213/evaluation-service/logs"
AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJhbnVzaHdhdGhpcmFuZ2FuYXRoYW5AZ21haWwuY29tIiwiZXhwIjoxNzgyODAzNjgzLCJpYXQiOjE3ODI4MDI3ODMsImlzcyI6IkFmZm9yZCBNZWRpY2FsIFRlY2hub2xvZ2llcyBQcml2YXRlIExpbWl0ZWQiLCJqdGkiOiJjNTNkMmRlMS1hOWNiLTQ0ZTctYWEyNi00ZmJjYTM0MDQwZDAiLCJsb2NhbGUiOiJlbi1JTiIsIm5hbWUiOiJhbnVzaHdhdGhpIHIiLCJzdWIiOiJhMWVjOTgyZi1kZjg5LTQ0OWUtYWUyOS0wMDhhNmM4NmU1ZjMifSwiZW1haWwiOiJhbnVzaHdhdGhpcmFuZ2FuYXRoYW5AZ21haWwuY29tIiwibmFtZSI6ImFudXNod2F0aGkgciIsInJvbGxObyI6IjIzYWlhMDkiLCJhY2Nlc3NDb2RlIjoiV2pOeUNUIiwiY2xpZW50SUQiOiJhMWVjOTgyZi1kZjg5LTQ0OWUtYWUyOS0wMDhhNmM4NmU1ZjMiLCJjbGllbnRTZWNyZXQiOiJ0RHd1dkZhU1JXUFVtaHNOIn0.P2Oth7KGKt5uAz6s2inT9DMFaFfWM92YYP0ap-GNLVA"
VALLID_STACKS = {"backend", "frontend"}
VALID_LEVELS= {"debug", "info", "warn", "error", "fatal"}
VALID_PACKAGES = {
    "cache", "controller", "cron_job", "db", "domain", "handler",
    "repository", "route", "service",
    "api", "component", "hook", "page", "state",
    "auth", "config", "middleware", "utils"
}
def Log(stack:str, level:str, package:str, message:str):
    stack = stack.lower()
    level = level.lower()
    package = package.lower()

    if stack not in VALLID_STACKS:
        raise ValueError(f"Invalid stack for: {stack}")
    if level not in VALID_LEVELS:
        raise ValueError(f"Invalid level for: {level}")
    if package not in VALID_PACKAGES:
        raise ValueError(f"Invalid stack for: {package}")
    payload = {
        "stack" : stack,
        "level" : level,
        "package" : package,
        "message" : message
    }
    headers = {
        "Authorization" : f"Bearer {AUTH_TOKEN}",
        "Content-Type" : "application/json"
    }
    response = requests.post(LOG_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Log failed: {response.status_code} - {response.text}")
        return None
    
if __name__ == '__main__':
        result = Log("backend", "error", "handler", "receiver string, expected bool")
        print(result)


