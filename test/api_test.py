import requests

def fetch_random_activity(num_activities=10):
    """Returns a list of exciting activities to do with ."""

    url =  "http://www.boredapi.com/api/activity/"
    activities = []

    for _ in range(num_activities):
        activity_data = requests.get(url)
        activities.append(activity_data.json())

    return activities


def show_activities(activities):
    """Displays activities that were generated
        and # of participants if available."""

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

        print(message)

def run():
    """Main program."""

    print("\t\t++++ ACTIVITY GENERATOR ++++\n")
    print(" This program generates 10 random activities for you")

    while True:
        print("Generate activities? Y/n")
        response = input()

        if response.lower() == 'y':
            activities = fetch_random_activity()
            show_activities(activities)

        elif response.lower() == 'n':
            print("Have Fun!")
            break

if __name__ == '__main__':
    run()
