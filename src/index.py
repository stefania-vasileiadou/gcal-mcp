'''

index.py

Pydantic data model classes for Google Calendar objects

Author: Stefania Vassiliadou (Northwestern CE/CS '27)

'''
from datetime import datetime
from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional, List

class Calendar(BaseModel):
    summary: str = Field(..., description="The title of the calendar")
    description: Optional[str] = Field(None, description="The description of the calendar") 
    location: Optional[str] = Field(None, description="The location of the calendar") 
    time_zone: Optional[str] = Field(None, description="The time zone of the calendar", alias="timeZone") 
    etag: Optional[str] = Field(None, description="ETag for the calendar")
    primary: Optional[bool] = Field(None, description="Whether this is the primary calendar")

    class Config:
        validate_by_name = True  # Allows both time_zone and timeZone

class EventResponseStatus(str, Enum):
    needsAction = 'needsAction'
    declined = 'declined'
    tentative = 'tentative'
    accepted = 'accepted'

class EventAttendee(BaseModel):
    id: Optional[str] = Field(None, description="Opaque identifier of the attendee")
    email: Optional[str] = Field(None, description="The attendee's email address")
    display_name: Optional[str] = Field(None, description="The attendee's name", alias="displayName") 
    organizer: Optional[bool] = Field(False, description="Whether the attendee is the organizer of the event")
    self: Optional[bool] = Field(False, description="Whether this entry represents the calendar on which this copy of the event appears")
    resource: Optional[bool] = Field(False, description="Whether the attendee is a resource")
    optional: Optional[bool] = Field(False, description="Whether this is an optional attendee")
    response_status: Optional[EventResponseStatus] = Field(None, description="The attendee's response status", alias="responseStatus")
    comment: Optional[str] = Field(None, description="The attendee's response comment")
    additional_guests: Optional[int] = Field(0, description="Number of additional guests", alias="additionalGuests")
    
    class Config:
        validate_by_name = True
        validate_assignment = True

class EventTimeStamp(BaseModel):
    date: Optional[datetime] = Field(None, description="The date, in the format 'yyyy-mm-dd', if this is an all-day event")
    date_time: Optional[datetime] = Field(None, description="The time, as a combined date-time value (formatted according to RFC3339)", alias="dateTime")
    time_zone: Optional[str] = Field(None, description="The time zone in which the time is specified (Formatted as an IANA Time Zone Database name, e.g. 'Europe/Zurich')", alias="timeZone")

    class Config:
        validate_by_name = True
        validate_assignment = True

class EventOrganizer(BaseModel):
    email: Optional[str] = Field(None, description="The organizer's name")
    display_name: Optional[str] = Field(None, description="The organizer's name", alias="displayName") 
    self: Optional[bool] = Field(False, description="Whether this entry represents the calendar on which this copy of the event appears")

class Event(BaseModel):
    kind: str = "calendar#event"
    id: Optional[str] = Field(None, description="Opaque identifier of the event")
    html_link: Optional[str] = Field(None, description="An absolute link to this event in the Google Calendar Web UI", alias="htmlLink")
    summary: Optional[str] = Field(None, description="Title of the event")
    organizer: Optional[EventOrganizer] = Field(None, description="The organizer of the event")
    description: Optional[str] = Field(None, description="The description of the event")
    location: Optional[str] = Field(None, description="Geographic location of the event as free-form text")
    color_id: Optional[str] = Field(None, description="The color of the event", alias="colorId")
    created: datetime = Field(..., description="Creation time of the event (as a RFC3339 timestamp)")
    updated: Optional[datetime] = Field(None, description="Last modification time of the main event data (as a RFC3339 timestamp)")
    start: Optional[EventTimeStamp] = Field(None, description="The (inclusive) start time of the event")
    end: Optional[EventTimeStamp] = Field(None, description="The (exclusive) end time of the event")
    attendees: Optional[List[EventAttendee]] = Field(None, description="The attendees of the event")
    attendees_omitted: Optional[bool] = Field(False, description="Whether attendees may have been omitted from the event's representation", alias="attendeesOmitted")

    class Config:
        validate_by_name = True 