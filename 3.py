from __future__ import print_function
import os.path
import base64
import email
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import openpyxl

# If modifying scopes, delete token.json
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_service():
    """Authenticate and return Gmail API service"""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def get_emails():
    """Fetch emails and return list of dictionaries"""
    service = get_service()
    results = service.users().messages().list(userId='me', maxResults=50).execute()
    messages = results.get('messages', [])

    email_data = []

    for msg in messages:
        msg_obj = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
        headers = msg_obj['payload']['headers']

        email_info = {
            "From": "",
            "To": "",
            "Subject": "",
            "Date": ""
        }

        for header in headers:
            name = header['name']
            if name == 'From':
                email_info['From'] = header['value']
            elif name == 'To':
                email_info['To'] = header['value']
            elif name == 'Subject':
                email_info['Subject'] = header['value']
            elif name == 'Date':
                email_info['Date'] = header['value']

        email_data.append(email_info)

    return email_data

def save_to_excel(email_data):
    """Save emails into XLSX file"""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Emails"

    # Header row
    ws.append(["From", "To", "Subject", "Date"])

    # Data rows
    for mail in email_data:
        ws.append([mail['From'], mail['To'], mail['Subject'], mail['Date']])

    wb.save("emails.xlsx")
    print("✅ Emails saved to emails.xlsx")

if __name__ == '__main__':
    data = get_emails()
    save_to_excel(data)
