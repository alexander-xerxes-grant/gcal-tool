import json
from datetime import datetime
from datetime import timezone

schedule_json = {
  "events": [
    {
      "summary": "Morning Exercise",
      "start_time": "2024-02-17T06:00:00",
      "end_time": "2024-02-17T07:00:00"
    },
    {
        "summary": "Coding Practice",
        "start_time": "2025-02-17T08:00:00",
        "end_time": "2025-02-17T09:00:00"
    }
  ]
}

def date_format(timestamp):
    d = datetime.fromisoformat(timestamp).astimezone(timezone.utc)
    return d.strftime('%H:%M %a-%d-%m-%Y')

events = schedule_json['events']
print(events)
for event in events:
    event_name = event["summary"]
    event_start_time = date_format(event["start_time"])
    event_end_time = date_format(event["end_time"])
    print(f"Title:{event_name}")
    print(f"Start: {event_start_time}")
    print(f"End: {event_end_time}")



