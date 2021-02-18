from __future__ import print_function
import datetime
import os
from googleapiclient.discovery import build
from prettytable import PrettyTable

from dotenv import load_dotenv

load_dotenv()


def main(arg):
    sol = ""
    # sol = PrettyTable()
    # sol.field_names = ["Fecha", "Evento"]

    service = build("calendar", "v3", developerKey=os.getenv("CALENDAR_TOKEN"))

    # Llama a la API del calendario
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indica UTC time
    print("Getting the upcoming 10 events")
    if arg:
        events_result = (
            service.events()
            .list(
                calendarId="qd0k8epqdam5jg2ldgpq6vu79vq5hbk8@import.calendar.google.com",
                timeMin=now,
                maxResults=10,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
    else:
        events_result = (
            service.events()
            .list(
                calendarId="p2q8lhhkk4jsugqeagv7iug2mnv2avup@import.calendar.google.com",
                timeMin=now,
                maxResults=10,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
    events = events_result.get("items", [])

    if not events:
        print("No upcoming events found.")
    for event in events:
        start = event["start"].get("dateTime", event["start"].get("date"))
        start = start.replace("Z", "").replace("T", " ")
        print(start, event["summary"])
        # sol.add_row((start, event['summary']))
        sol += "  ".join((start, event["summary"]))
        sol += "\n"
    return sol  # .get_string()


if __name__ == "__main__":
    main()
