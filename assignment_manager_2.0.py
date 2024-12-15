"""
Luke Cirne
Assignment Manager 2.0
Google Calendar Integration
"""
import array
import math
import datetime
import os.path
import sys

from datetime import timezone
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Calendar Permissions
SCOPES = ["https://www.googleapis.com/auth/calendar"]

def main():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
   
    try:
        service = build("calendar", "v3", credentials=creds)
    except HttpError as error:
        print(f"An error occurred: {error}")


    # Call the Calendar API
    current_datetime = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time

def add_assignment(course, assignment_name, due_date):
    if course_name in course_dict.keys():
        course_dict[course].append((assignment_name, due_date))
        return True
    return False

