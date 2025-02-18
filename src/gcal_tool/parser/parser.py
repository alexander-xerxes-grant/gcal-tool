import json
from datetime import datetime, timezone
from typing import Any, Dict, Iterator

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

    def parse_date(self, timestamp_str: str) -> datetime:
        """Convert an ISO format string to a datetime object in UTC."""
        # This handles strings like "2024-02-17T06:00:00"
        return datetime.fromisoformat(timestamp_str).astimezone(timezone.utc)

    def parse_schedule(self, schedule_json: dict) -> CalendarEvent:
        events = schedule_json["events"]
        for event in events:
            CalendarEvent.event_summary = event["summary"]
            CalendarEvent.start_time = self.parse_date(event["start_time"])
            CalendarEvent.end_time = self.parse_date(event["end_time"])
            return CalendarEvent
