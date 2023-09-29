import requests
import tkinter as tk

def fetch_random_activity():
    """Returns a list of exciting activities to do."""

    url =  "http://www.boredapi.com/api/activity/"
    num_activities = 10
    activities = [] # List to store all activity data

    for _ in range(num_activities):
        activity_data = requests.get(url)
        activities.append(activity_data.json())

    return activities

def show_activities(activities):
    """Displays activities that were generated
        and # of participants if available."""
    result = ""

    for idx, item in enumerate(activities, start=1):
        activity = item['activity']
        category = item['type']
        participants = item['participants']
        message = f"{idx}. Category: {category} - {activity}"
        link_to = item['link']
        if participants > 2:
            message += f" - Total participants: {participants}"
        if link_to:
            message += f". Link: {link_to}"

        result += message + "\n\n"

    return result

def update_text_widget(text_widget, results):
    text_widget.delete("1.0", tk.END)
    text_widget.insert(tk.END, results)
