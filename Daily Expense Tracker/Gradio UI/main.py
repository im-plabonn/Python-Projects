import gradio as gr
import os
import json
from datetime import datetime as dt
from google.oauth2 import service_account
from googleapiclient.discovery import build

# --- Google Sheets Setup (Using Secrets) ---
def get_sheet_service():
    # Hugging Face-er Secret theke credentials nibe
    creds_json = os.getenv("G_CREDS") 
    creds_dict = json.loads(creds_json)
    
    creds = service_account.Credentials.from_service_account_info(creds_dict)
    service = build('sheets', 'v4', credentials=creds)
    return service.spreadsheets()

SPREADSHEET_ID = os.getenv("SHEET_ID")

def add_expense(amount, category):
    # Empty check: User jodi kicu na likhe submit kore
    if not category or amount <= 0:
        return "Please enter a valid amount and category name."
        
    try:
        sheet = get_sheet_service()
        today = dt.now().strftime("%d/%m/%Y")
        
        # Data format for Google Sheets
        values = [[today, category.strip(), amount]]
        body = {'values': values}
        
        sheet.values().append(
            spreadsheetId=SPREADSHEET_ID,
            range="Sheet1!A1",
            valueInputOption="USER_ENTERED",
            insertDataOption="INSERT_ROWS",
            body=body
        ).execute()
        return f"Success! Saved {amount} TK in '{category}'"
    except Exception as e:
        return f"Error: {str(e)}"

# --- Gradio UI ---
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# My Personal Expense Tracker")
    gr.Markdown("Enter your expense details below to save them directly to Google Sheets.")
    
    with gr.Row():
        amt = gr.Number(label="Expense Amount", value=0)
        # Dropdown-er jaygay Textbox bebohar kora hoyeche
        cat = gr.Textbox(label="Category (e.g., Food, Rent, Marketing)", placeholder="Type category name...")
    
    submit_btn = gr.Button("Submit to Google Sheets", variant="primary")
    output = gr.Textbox(label="Status")

    # Function call
    submit_btn.click(fn=add_expense, inputs=[amt, cat], outputs=output)

demo.launch()
