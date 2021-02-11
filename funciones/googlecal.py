from __future__ import print_function
import datetime
import os
from googleapiclient.discovery import build

from dotenv import load_dotenv

load_dotenv()


def main():
    sol = ''
    # print(os.getenv('CALENDAR_TOKEN'))

    service = build('calendar', 'v3', developerKey=os.getenv('CALENDAR_TOKEN'))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='qd0k8epqdam5jg2ldgpq6vu79vq5hbk8@import.calendar.google.com', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
        sol += '  '.join((start, event['summary']))
        sol += '\n'
    return sol



if __name__ == '__main__':
    main()
