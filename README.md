# 📧 AI Email Agent Automation 🤖

An intelligent Python-based AI Email Agent that automatically composes and sends professional emails using natural language commands. Just tell it:
 
----->    write a mail to someone@example.com on subject: Project Update     <------


…and it handles the rest using AI and Gmail API!
## 🚀 Features

- 💡 Generates email content using Cohere LLM
- 📬 Sends emails via Gmail API
- 🔠 Extracts recipient name from email automatically
- 🧠 Understands natural language commands
- ✅ Fully automated from command to delivery

## 🛠️ Tech Stack

- Python 3.12+
- [Cohere API](https://cohere.com/)
- Gmail API (Google Cloud)
- Google OAuth2
- Regex & MIME for formatting

---

## 🔧 Setup Instructions

### 1. Clone the Repository

git clone https://github.com/msnanda229/Ai_Email_Agent_Automation.git
cd Ai_Email_Agent_Automation


2.  Install Required Packages

python -m pip install cohere google-auth google-auth-oauthlib google-api-python-client


3. Get Gmail API credentials.json
Go to Google Cloud Console

Create a new project

Enable the Gmail API

Configure OAuth consent screen

Create OAuth Client ID → Type: Desktop App

Download credentials.json and place it in your project folder

4. Run the Script

python mail.py

✨ How to Use
Once the agent is running, type:

write a mail to friend@gmail.com on subject: Happy Birthday!
The agent will:

Parse the command

Generate a professional email

Send it via your Gmail account

Type exit to stop the agent.

📁 Project File Structure

Ai_Email_Agent_Automation/
├── mail.py                 # Main Python script for the AI Email Agent
├── credentials.json        # OAuth credentials file from Google
├── token.json              # Auto-generated token after authentication


🤝 Made With
Built with the help of ChatGPT for rapid coding, debugging, and idea refinement.

📫 Connect
Made with ❤️ by Shanmukha Nanda
Follow me on https://www.linkedin.com/in/medisetty-shanmukha-nanda-907798291/


