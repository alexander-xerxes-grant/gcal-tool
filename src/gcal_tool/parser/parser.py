"""Parser for Google Calendar events."""

import json
from dataclasses import dataclass
from datetime import datetime


class CalendarEventError(Exception):
    """Raised when calendar event validation fails."""

    pass


@dataclass
class CalendarEvent:
    """
    Represents a calendar event with a start time,
    end_time and summary.
    """

    event_summary: str
    start_time: datetime
    end_time: datetime
    calendar_id: str | None = None  # Optional with a default of None

    def __post_init__(self) -> None:
        """Validate the event times after intialisation."""
        if self.end_time <= self.start_time:
            raise CalendarEventError(
                f"End time ({self.end_time})"
                f"must be after start time({self.start_time})."
            )


class JSONParser:
    """Parser for Google Calendar events."""

    def parse_json(json_object: dict) -> dict:
        """Parse the schedule input as a JSON into an event object."""
        # Not sure what parts of the JSON
        # will be required yet
        event = json.loads(json_object)
        return event


class GoogleCalendarClient:
    """Client for interacting with the Google calendar API."""

    def insert_event(event: dict) -> None:
        """Insert an event into a calendar."""
        # makes api call to the gcal api
        # passes the event to the API which
        # inserts with the metadata it contains
        ###I basically need something that takes an input,
        #  then parses that into a request that the Google API will accept.
        ### The only required properties in the request
        #  are the start and end time so lets start with that
        pass
