import os
import pandas as pd
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# Load credentials
creds = Credentials.from_authorized_user_file("token.json", ["https://www.googleapis.com/auth/gmail.readonly"])
service = build("gmail", "v1", credentials=creds)

# Labels you want to export separately
CATEGORY_LABELS = {
    "primary": "CATEGORY_PERSONAL",
    "promotions": "CATEGORY_PROMOTIONS",
    "drafts": "DRAFT",
    "inbox": "INBOX",
    "sent": "SENT"
}

def fetch_emails_by_label(label_id):
    emails_data = []
    results = service.users().messages().list(userId="me", labelIds=[label_id], maxResults=50).execute()
    messages = results.get("messages", [])

    for msg in messages:
        msg_data = service.users().messages().get(userId="me", id=msg["id"], format="metadata", metadataHeaders=["From", "Subject", "Date"]).execute()
        headers = msg_data.get("payload", {}).get("headers", [])
        email_info = {"From": "", "Subject": "", "Date": ""}
        for header in headers:
            if header["name"] in email_info:
                email_info[header["name"]] = header["value"]
        emails_data.append(email_info)
    
    return emails_data

# Create a folder to store Excel files
os.makedirs("gmail_reports", exist_ok=True)

# Fetch & save each category separately
for category_name, label_id in CATEGORY_LABELS.items():
    data = fetch_emails_by_label(label_id)
    df = pd.DataFrame(data)
    file_path = f"gmail_reports/{category_name}_emails.xlsx"
    df.to_excel(file_path, index=False)
    print(f"✅ Saved: {file_path}")
