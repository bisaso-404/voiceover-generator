from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Permissions: Sheets read + Drive write
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://www.googleapis.com/auth/drive.file"
]

def get_google_services():
    """Authenticate user and return Sheets + Drive clients."""
    creds = None

    # token.json stores user session after first login
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If no creds, or expired, do OAuth
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    sheets_service = build("sheets", "v4", credentials=creds)
    drive_service = build("drive", "v3", credentials=creds)

    return sheets_service, drive_service

def get_sheet_names(sheet_id):
    """Get all sheet names from a Google Spreadsheet."""
    sheets_service, _ = get_google_services()
    
    result = sheets_service.spreadsheets().get(spreadsheetId=sheet_id).execute()
    sheets = result.get('sheets', [])
    
    return [sheet['properties']['title'] for sheet in sheets]



def read_sheet(sheet_id, range_name):
    """Reads data rows from a Google Sheet."""
    sheets_service, _ = get_google_services()
    
    result = sheets_service.spreadsheets().values().get(
        spreadsheetId=sheet_id,
        range=range_name
    ).execute()

    return result.get("values", [])

def upload_to_drive(file_path, parent_folder_id):
    """Upload generated mp3 to Google Drive."""
    _, drive_service = get_google_services()

    file_metadata = {
        "name": os.path.basename(file_path),
        "parents": [parent_folder_id]
    }

    media = MediaFileUpload(file_path, mimetype="audio/mpeg")

    uploaded_file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id"
    ).execute()

    return uploaded_file["id"]
