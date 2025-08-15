# Gmail Email Extractor 📧

A Python automation script that connects to your Gmail account via the official **Gmail API**, fetches emails from different categories (Primary, Social, Promotions, Drafts, etc.), and saves them into separate **Excel (.xlsx)** files.

---

## ✨ Features

- **OAuth 2.0 authentication** (Google API)
- Fetches emails from Gmail by category:
  - Primary
  - Social
  - Promotions
  - Drafts
- Saves each category into **separate Excel files**
- Properly formatted Excel output (Date, Sender, Subject, Snippet)
- Handles empty/null values gracefully

---

## 🛠 Requirements

- Python 3.8+
- A Google Cloud project with Gmail API enabled
- Installed dependencies:

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib openpyxl
```

🚀 How to Use

Enable Gmail API in Google Cloud:
Go to: https://console.cloud.google.com/
Create a new project
Enable the Gmail API
Create OAuth client credentials
Download credentials.json
Place the credentials file in your project folder.

Run the script for the first time:

```bash
python main.py
```

A browser window will open to authenticate your Google account.
This will generate a token.json file for future runs.
Check the output Excel files will be saved in the current directory:
primary_emails.xlsx
social_emails.xlsx
promotions_emails.xlsx
draft_emails.xlsx

---

📜 License

MIT License – Free to use and modify.

🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you'd like to change.

---

💡 Author

Muhammad Shoaib – Backend Developer (Django, Python)
