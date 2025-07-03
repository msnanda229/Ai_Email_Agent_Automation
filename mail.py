import os
import base64
import re
import cohere
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request  # ✅ Added this import

# Cohere Initialization
co = cohere.Client("f94offoyreBTTwrJ8pJfCnXNSjEqiGUFrwM6ElFU")

# Gmail API Scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Step 1: Authenticate Gmail
def authenticate_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())  # ✅ Fixed here
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

# Step 2: Format recipient name from email
def format_name_from_email(email):
    username = email.split("@")[0]
    parts = re.split(r'[._\-]', username)
    formatted = " ".join(part.capitalize() for part in parts)
    return formatted

# Step 3: Generate email body using Cohere
def generate_email_body(subject, recipient_email):
    name = format_name_from_email(recipient_email)
    signature = "\n\nBest regards,\nShanmukha Nanda\nCEO\nMSN Solutions"

    prompt = (
        f"Write a professional and sincere email to {name} with the subject: '{subject}'. "
        f"The email should begin with a greeting like 'Dear {name},' and should not repeat it. "
        f"Express appreciation or gratitude and end politely."
    )

    response = co.generate(
        model="command-r-plus",
        prompt=prompt,
        max_tokens=200,
        temperature=0.7
    )

    body = response.generations[0].text.strip()
    return body + signature

# Step 4: Create raw email message
def create_message(to, subject, body):
    message = MIMEText(body)
    message['to'] = to
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw}

# Step 5: Send the email via Gmail API
def send_email(service, to_email, subject, body):
    try:
        message = create_message(to_email, subject, body)
        send_message = service.users().messages().send(userId="me", body=message).execute()
        print(f"✅ Email sent to {to_email} with subject: {subject}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

# Step 6: Parse command
def parse_command(command):
    match = re.search(r"write a mail to (.+?) (on|with) subject[:\-]? (.+)", command, re.IGNORECASE)
    if match:
        to_email = match.group(1).strip()
        subject = match.group(3).strip()
        return to_email, subject
    return None, None

# Step 7: Full AI agent logic
def ai_email_agent(command):
    to_email, subject = parse_command(command)
    if to_email and subject:
        body = generate_email_body(subject, to_email)
        service = authenticate_gmail()
        send_email(service, to_email, subject, body)
    else:
        print("❌ Invalid command format. Try: write a mail to xyz@gmail.com on subject: Hello")

# Run the agent
print("🤖 Auto Email Agent Ready (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    ai_email_agent(user_input)
