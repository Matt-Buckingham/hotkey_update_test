import os

from google.auth.transport.requests import Request
from google.oauth2.credntials import Credentials
from google_auth_oauth2.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = "1pMHspLuX6sGFGPi0Q-PLy-A7a-Kvbi9tG4bI7CzpF5A"

def main():
    credentials = None
    if os.path.exists("token.json")
            