Daily Expense Tracker
A Python-based automation tool that allows users to log their daily expenses through a web interface and automatically saves the data to a Google Sheet. This project leverages the Google Sheets API for data persistence and Gradio for a user-friendly web interface.

Live Demo
You can access the live application here: Daily Expense Tracker on Hugging Face

Features
Interactive Web Interface: Built with Gradio for easy data entry.

Custom Category Support: Users can manually enter any category name for their expenses.

Automated Date Logging: Automatically captures the current date for every entry.

Google Sheets Integration: Real-time data synchronization using the Google Sheets API.

Secure Credential Management: Uses environment variables (Secrets) to handle sensitive API keys.

Technologies Used
Python: Core programming language.

Gradio: For creating the web-based user interface.

Google Sheets API: For cloud-based data storage.

Google Auth: For secure service account authentication.

Hugging Face Spaces: For hosting the application.

Project Structure
Plaintext
Automato-Hub/
├── 01_Expense_Tracker/
│   ├── app.py              # Main application code
│   └── requirements.txt    # List of required Python libraries
├── .gitignore              # To prevent sensitive files from being uploaded
└── README.md               # Project documentation
Setup and Installation
Prerequisites
A Google Cloud Project with the Google Sheets API enabled.

A Service Account with a generated JSON key file.

A Google Sheet shared with the Service Account's email address.

Local Setup
Clone the repository:

Bash
git clone https://github.com/your-username/Automato-Hub.git
Navigate to the project folder:

Bash
cd 01_Expense_Tracker
Install dependencies:

Bash
pip install -r requirements.txt
Place your credentials.json file in the root directory.

Set up your environment variables for SHEET_ID.

Run the application:

Bash
python app.py
Security Note
This project follows security best practices by not including the credentials.json file in the version control system. For cloud deployment (like Hugging Face), credentials must be stored in the platform's Secrets/Environment Variables section as a string.

Author
Habibur Rahman Plabon
Computer Science and Engineering Student at Feni University
