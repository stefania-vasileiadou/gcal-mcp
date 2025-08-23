'''

tools.py

Collection of MCP tools that communicate with the Google Calendar API using syntax 
provided by the `google-api-python-client tutorial` package.

Author: Stefania Vassiliadou (Northwestern CE/CS '27)

'''
from auth import get_service
import logging
import datetime

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials

logger = logging.getLogger()
now = datetime.datetime.now(tz=datetime.timezone.utc).isoformat()

def get_events(calendar_id: str = "primary", time_min: str = now, 
                         time_max: str = None, query: str = None,
                         max_results: int = 50):
    service = get_service()
    if not service:
        return None
    
    try:
        events_result = (
            service.events()
            .list(
                calendarId=calendar_id,
                timeMin=time_min,
                time_max=time_max,
                maxResults=max_results,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])

        if not events:
            print("No upcoming events found.")
            return

        logger.info(f"Fetched {len(events)} events")

        return events

    except HttpError as e:
        logger.error(f"An error occurred: {e}")


def list_calendars(min_access_role: str = "reader"):
    service = get_service()
    if not service:
        return None
    
    try:
        now = datetime.datetime.now(tz=datetime.timezone.utc).isoformat()

        calendars_result = (
            service.calendarList()
            .list(
                minAccessRole=min_access_role
            )
            .execute()
        )
        calendars = calendars_result.get("items", [])

        if not calendars:
            print("No calendars found.")
            return

        logger.info(f"Fetched {len(calendars)} calendars")

        return calendars

    except HttpError as e:
        logger.error(f"An error occurred: {e}")