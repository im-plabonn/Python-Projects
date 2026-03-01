import gradio as gr

def calculate_bmi(name, weight, height_cm):
    try:
        # Height-ke meter-e convert kora (User height cm-e dibe)
        height_m = height_cm / 100
        bmi = weight / (height_m * height_m)
        
        # BMI Category nirnoy
        if bmi < 18.5:
            status = "Underweight (অল্প ওজন) 🟡"
            advice = "You should eat a balanced diet and consult a nutritionist."
        elif 18.5 <= bmi < 24.9:
            status = "Normal (সঠিক ওজন) ✅"
            advice = "Great job! Maintain your current lifestyle."
        elif 25 <= bmi < 29.9:
            status = "Overweight (অতিরিক্ত ওজন) 🟠"
            advice = "Try to include more physical activity in your routine."
        elif 30 <= bmi < 34.9:
            status = "Obese (স্থূলতা) 🔴"
            advice = "Consider a structured weight loss plan and exercise."
        else:
            status = "Extremely Obese (অত্যধিক স্থূলতা) 🛑"
            advice = "Please consult a doctor for a health checkup."

        result_text = f"Dear {name}, Your BMI is: {bmi:.2f}"
        return result_text, status, advice
    except ZeroDivisionError:
        return "Error", "Height cannot be zero!", ""

# Gradio UI Design
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🏥 Personal BMI Calculator")
    gr.Markdown("Enter your details below to check your Body Mass Index (BMI).")
    
    with gr.Row():
        with gr.Column():
            name_input = gr.Textbox(label="Your Name", placeholder="Enter your name here...")
            weight_input = gr.Number(label="Weight (kg)", value=70)
            height_input = gr.Slider(label="Height (cm)", minimum=50, maximum=250, value=170, step=1)
            submit_btn = gr.Button("Calculate BMI", variant="primary")
        
        with gr.Column():
            bmi_output = gr.Textbox(label="Result", interactive=False)
            status_output = gr.Textbox(label="Status", interactive=False)
            advice_output = gr.Textbox(label="Health Advice", interactive=False)

    # Button Click Event
    submit_btn.click(
        fn=calculate_bmi, 
        inputs=[name_input, weight_input, height_input], 
        outputs=[bmi_output, status_output, advice_output]
    )

# Launch the app
if __name__ == "__main__":
    demo.launch()