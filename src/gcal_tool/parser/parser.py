import json
from datetime import datetime, timezone
from main import CalendarEvent

schedule_json = {
    "events": [
        {
            "summary": "Morning Exercise",
            "start_time": "2024-02-17T06:00:00",
            "end_time": "2024-02-17T07:00:00",
        },
        {
            "summary": "Coding Practice",
            "start_time": "2025-02-17T08:00:00",
            "end_time": "2025-02-17T09:00:00",
        },
    ]
}


class ScheduleParser:
    """Parse a schedule JSON object into an event object."""

    def format_date(self, timestamp: datetime) -> datetime:
        d = datetime.fromisoformat(timestamp).astimezone(timezone.utc)
        return d.strftime("%H:%M %a-%d-%m-%Y")

    def parse_schedule(self, schedule_json: dict) -> CalendarEvent:
        events = schedule_json[events]
        for event in events:
            CalendarEvent.event_summary = event["summary"]
            CalendarEvent.start_time = self.format_date(event["start_time"])
            CalendarEvent.end_time = self.format_date(event["end_time"])
            return CalendarEvent
