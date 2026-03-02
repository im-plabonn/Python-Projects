# 🏏 Cricket Net Run Rate Calculator

A simple and interactive **Net Run Rate (NRR) Calculator** built using **Python + Gradio UI**.  
This tool calculates the NRR of two cricket teams based on match statistics.

🔗 **Live App:** https://huggingface.co/spaces/im-plabonn/net_run_rate_calculator

---

## 📌 Features
- Clean and responsive Gradio interface
- Calculates NRR for both teams instantly
- Error handling for invalid overs (division by zero)
- Decimal precision up to 3 places
- Beginner-friendly and readable code structure

---

## 🧠 What is Net Run Rate (NRR)?

Net Run Rate is a statistical method used in cricket tournaments to rank teams with equal points.

**Formula used:**
NRR = (Runs Scored ÷ Overs Faced) − (Runs Conceded ÷ Overs Bowled)


Since this calculator compares **two teams in a single match**, calculation is simplified as:
Team1 NRR = (Team1 Runs / Team1 Overs) − (Team2 Runs / Team2 Overs)
Team2 NRR = − (Team1 NRR)


---

## ⚙️ How the Calculation Works (Logic Flow)

1. User enters:
   - Team names
   - Match overs
   - Runs scored
   - Overs faced

2. System calculates:
   - Run rate for each team  
   - Difference between both run rates  

3. Returns:
   - Team1 NRR  
   - Team2 NRR (negative of Team1 NRR)

4. Handles edge case:
   - If overs = 0 → shows error message

---

## 🏗 Tech Stack
- Python
- Gradio (Blocks UI API)
- Hosted on Hugging Face Spaces

---
