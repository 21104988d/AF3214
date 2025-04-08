import requests
import time
import csv
from datetime import datetime

def send_telegram_message(message):
    # Replace 'your_bot_token' and 'your_chat_id' with actual values
    bot_token = "7736940759:AAHTTMKKHJXh3atC2xDgxxKt7iFSdhrqNes"
    chat_id = "266564928"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to send message: {e}")

processed_message_ids = set()
def receive_telegram_messages():
    # Replace 'your_bot_token' with the actual bot token
    bot_token = "7736940759:AAHTTMKKHJXh3atC2xDgxxKt7iFSdhrqNes"
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    try:
        response = requests.get(url)
        response.raise_for_status()
        updates = response.json()
        if "result" in updates:
            messages = updates["result"]
            new_messages = [message for message in messages if message["message"]["message_id"] not in processed_message_ids]
            
            if new_messages:
                with open("telegram_messages.csv", mode="a", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    # Write header if the file is empty
                    if file.tell() == 0:
                        writer.writerow(["Receive ID", "Time", "Message"])
                    for message in new_messages:
                        if "message" in message:
                            receive_id = message["message"]["message_id"]
                            timestamp = datetime.fromtimestamp(message["message"]["date"]).strftime('%Y-%m-%d %H:%M:%S')
                            text = message["message"].get("text", "")
                            writer.writerow([receive_id, timestamp, text])
                            processed_message_ids.add(receive_id)
            return new_messages
        else:
            print("No messages found.")
            return []
    except requests.RequestException as e:
        print(f"Failed to receive messages: {e}")
        return []