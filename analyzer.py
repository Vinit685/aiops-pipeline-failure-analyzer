import requests
import sys

TELEGRAM_TOKEN = "8733103302:AAFNXvZQM9Zvm7zsluVWsL8UgmlQHs-5eEE"
TELEGRAM_CHAT_ID = "7370899892"

def analyze_log(log_text):
    prompt = f"""
    You are a DevOps engineer. Analyze this CI/CD build log and respond with:
    1. Root Cause (1 sentence)
    2. Error Type (one of: dependency, docker, test, network, config)
    3. Suggested Fix (2-3 bullet points)

    Log:
    {log_text[-3000:]}
    """

    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "tinyllama",
        "prompt": prompt,
        "stream": False
    })

    return response.json()["response"]

def send_to_telegram(diagnosis):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": f"🔴 AIOps Build Failure Diagnosis:\n\n{diagnosis}"
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    log = sys.stdin.read()
    diagnosis = analyze_log(log)
    print(diagnosis)
    send_to_telegram(diagnosis)
