<h1 align="center">💸 Daily Expense Tracker</h1>

<p align="center">
A Python-based automation tool that allows users to log daily expenses through a web interface and automatically store the data in Google Sheets.
</p>

<hr>

<h2>Live Demo</h2>

<p>
Try it here:<br>
<a href="https://huggingface.co/spaces/im-plabonn/bmi](https://huggingface.co/spaces/im-plabonn/Daily-Expense-Tracker" target="_blank">
Daily Expense Tracker on Hugging Face
</a>
</p>

<hr>

<h2>Features</h2>

<ul>
<li><b>Interactive Web Interface</b> – Built with Gradio for smooth and easy data entry.</li>
<li><b>Custom Category Support</b> – Users can manually enter any expense category.</li>
<li><b>Automated Date Logging</b> – Automatically records the current date with each entry.</li>
<li><b>Real-Time Google Sheets Sync</b> – Integrated with Google Sheets API for instant cloud storage.</li>
<li><b>Secure Authentication</b> – Uses environment variables (Secrets) to protect sensitive credentials.</li>
<li><b>Cloud Deployment</b> – Hosted on Hugging Face Spaces for public access.</li>
</ul>

<hr>

<h2>Technologies Used</h2>

<ul>
<li><b>Python</b> – Core programming language</li>
<li><b>Gradio</b> – Web interface creation</li>
<li><b>Google Sheets API</b> – Cloud-based data storage</li>
<li><b>Google Auth</b> – Secure service account authentication</li>
<li><b>Hugging Face Spaces</b> – Application hosting</li>
</ul>

<hr>

<h2>Project Structure</h2>

<pre>
Automato-Hub/
├── 01_Expense_Tracker/
│   ├── app.py
│   └── requirements.txt
├── .gitignore
└── README.md
</pre>

<hr>

<h2>Setup and Installation</h2>

<h3>Prerequisites</h3>

<ul>
<li>A Google Cloud Project with Google Sheets API enabled</li>
<li>A Service Account with a generated JSON key file</li>
<li>A Google Sheet shared with the Service Account’s email</li>
</ul>

<h3>Local Setup</h3>

<p><b>Clone the Repository</b></p>

<pre>
git clone https://github.com/your-username/Automato-Hub.git
</pre>

<p><b>Navigate to the Project Folder</b></p>

<pre>
cd 01_Expense_Tracker
</pre>

<p><b>Install Dependencies</b></p>

<pre>
pip install -r requirements.txt
</pre>

<p><b>Add Credentials</b></p>

<ul>
<li>Place your <code>credentials.json</code> file in the root directory</li>
<li>Set environment variable for <code>SHEET_ID</code></li>
</ul>

<p><b>Run the Application</b></p>

<pre>
python app.py
</pre>

<hr>

<h2>Security Best Practices</h2>

<ul>
<li>The <code>credentials.json</code> file is excluded from version control using <code>.gitignore</code></li>
<li>For cloud deployment (Hugging Face Spaces), credentials must be stored in the platform's Secrets section</li>
<li>No sensitive API keys are publicly exposed</li>
</ul>

<hr>

<h2>Author</h2>

<p>
<b>Habibur Rahman Plabon</b><br>
Computer Science & Engineering Student<br>
Feni University
</p>

<hr>

<p align="center">
⭐ If you like this project, consider giving it a star!
</p>
