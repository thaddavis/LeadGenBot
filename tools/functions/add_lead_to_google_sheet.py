import gspread
import json
import os

from oauth2client.service_account import ServiceAccountCredentials


# Set up Google Sheets API credentials
def authenticate_gsheets():
    scope = "https://spreadsheets.google.com/feeds https://www.googleapis.com/auth/drive"

    print("!")

    # Read credentials from environment variable
    creds_json = os.getenv("GOOGLE_CREDENTIALS")

    print("!!")

    if not creds_json:
        raise ValueError(
            "❌ GOOGLE_CREDENTIALS not found in environment variables.")

    print("!!!")

    creds_dict = json.loads(creds_json)
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)

    print("!!!!")

    return client


# Append a row to a Google Spreadsheet
def add_lead_to_google_sheet(email: str, phone_number: str, notes: str):
    """
    Appends a row to a Google Sheet.
    """

    try:
        print("---> TOOL CALL: add_lead_to_google_sheet <---")
        client = authenticate_gsheets()
        spreadsheet_id = "1frcV3MUEsPHePcaxjEwfbtMOv6TRTFzej9y2Mx-ia64"
        sheet_name = "Sheet1"
        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
        sheet.append_row([email, phone_number, notes])
        return "Row added successfully!"
    except Exception as e:
        print(e)
        print(f"❌ Error: {str(e)}")
        return "Oops! An error occurred."
