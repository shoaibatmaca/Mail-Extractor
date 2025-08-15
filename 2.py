from __future__ import print_function
import os.path
import base64
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# If modifying these SCOPES, delete the file token.json
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic email list."""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    service = build('gmail', 'v1', credentials=creds)

    # Get first 50 emails
    results = service.users().messages().list(userId='me', maxResults=50).execute()
    messages = results.get('messages', [])

    if not messages:
        print("No messages found.")
    else:
        print("Messages:")
        for msg in messages:
            msg_detail = service.users().messages().get(userId='me', id=msg['id']).execute()
            headers = msg_detail['payload']['headers']
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), None)
            sender = next((h['value'] for h in headers if h['name'] == 'From'), None)
            date = next((h['value'] for h in headers if h['name'] == 'Date'), None)
            print(f"{date} | {sender} | {subject}")

if __name__ == '__main__':
    main()
