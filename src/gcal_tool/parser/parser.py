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

    def parse_event(self, event_data: Dict[str, Any]) -> CalendarEvent:
        """Parse a single event dictionary into a CalendarEvent object."""
        try:
            event_summary = event_data["summary"]
            start_time = self.parse_date(event_data["start_time"])
            end_time = self.parse_date(event_data["end_time"])

            return CalendarEvent(
                event_summary=event_summary,
                start_time=start_time,
                end_time=end_time
            )
        except KeyError as e:
            raise ValueError(f"Missing require field in event: {e}")


    def parse_schedule(self, schedule_json: Dict[str, Any]) -> CalendarEvent:
        """Parse a schedule JSON object into CalendarEvent objects.

        Args:
            schedule_json: A dictionary containing an 'events' key
            with a list of events
        
        Yields:
            CalendarEvent objects, one at a time

        Raises:
            ValueError: If the JSON is missing required fields 
        """
        events = schedule_json.get("events", [])

        for event in events:
            try:
                yield self.parse_event(event)
            except ValueError as e:
                raise ValueError(f"Failed to parse event: {e}")

