import gradio as gr

def check_password_strength(password):
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    special_characters = "@#$%^&*()_+-=[]{}|;:,.<>?/"
    has_special = any(char in special_characters for char in password)

    score = 0

    if len(password) >= 8:
        score += 1

    if has_upper: score += 1
    if has_lower: score += 1
    if has_digit: score += 1
    if has_special: score += 1

    if score <= 2:
        return f"Score: {score}/5 - Strength: Weak 🔴"
    elif score <= 4:
        return f"Score: {score}/5 - Strength: Medium 🟡"
    else:
        return f"Score: {score}/5 - Strength: Strong 🟢"

interface = gr.Interface(
    fn=check_password_strength,
    inputs=gr.Textbox(label="Enter Password", placeholder="Type your password here...", type="password"),
    outputs=gr.Textbox(label="Result"),
    title="Password Strength Checker",
    description="Check how strong your password is. This tool verifies the length, uppercase letters, numbers, and special characters."
)

if __name__ == "__main__":
    interface.launch()