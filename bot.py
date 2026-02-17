import requests
import csv
import time
import os

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

URL = f"https://api.telegram.org/bot{TOKEN}/sendPoll"

def send_quiz(question, options, correct_index):
    payload = {
        "chat_id": CHAT_ID,
        "question": question,
        "options": options,
        "type": "quiz",
        "correct_option_id": correct_index,
        "is_anonymous": False
    }
    r = requests.post(URL, json=payload)
    print(r.json())

with open("mcq.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        options = [
            row["option1"],
            row["option2"],
            row["option3"],
            row["option4"]
        ]
        correct = ["A","B","C","D"].index(row["answer"])
        send_quiz(row["question"], options, correct)
        time.sleep(1.3)
