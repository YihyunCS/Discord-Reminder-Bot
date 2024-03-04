import requests
import time

def discord_log(reminder):
    webhook_url = "YOURDISCORDWEBHOOKHERE"
    data = {"content": f"Reminder: {reminder}"}
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Reminder sent successfully.")
    else:
        print("Failed to send reminder.")

def main():
    reminder = input("Enter your reminder: ")
    timer_input = input("Enter the timer duration (e.g., '5 seconds' or '10 minutes'): ")
    duration, unit = timer_input.split()
    duration = int(duration)

    if unit.lower() == 'seconds':
        time.sleep(duration)
    elif unit.lower() == 'minutes':
        time.sleep(duration * 60)
    else:
        print("Invalid unit. Please use 'seconds' or 'minutes'.")
        return

    discord_log(reminder)

if __name__ == "__main__":
    main()
