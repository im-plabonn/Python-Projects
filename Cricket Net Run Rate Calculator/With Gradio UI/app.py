import gradio as gr

def calculate_nrr(team1_name, team2_name, match_overs, t1_runs, t1_overs_faced, t2_runs, t2_overs_faced):
    try:
        # Team 1 calculation
        team1_val = t1_runs / t1_overs_faced
        # Team 2 calculation
        team2_val = t2_runs / t2_overs_faced
        
        team1_nrr = team1_val - team2_val
        team2_nrr = -team1_nrr
        
        return f"{team1_name}: {team1_nrr:.3f}", f"{team2_name}: {team2_nrr:.3f}"
    except ZeroDivisionError:
        return "Error: Overs cannot be zero", "Error: Overs cannot be zero"

with gr.Blocks(title="Cricket NRR Calculator") as demo:
    gr.Markdown("# 🏏 Cricket Net Run Rate Calculator")
    gr.Markdown("Enter the match details below to calculate the NRR for both teams.")
    
    with gr.Row():
        team1_input = gr.Textbox(label="Team 1 Name", placeholder="e.g. Bangladesh")
        team2_input = gr.Textbox(label="Team 2 Name", placeholder="e.g. India")
    
    total_match_overs = gr.Number(label="Total Match Overs (e.g. 20 or 50)", value=20)
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Team 1 Stats")
            t1_runs = gr.Number(label="Runs Scored")
            t1_overs = gr.Number(label="Overs Faced (If All Out, enter total match overs)")
            
        with gr.Column():
            gr.Markdown("### Team 2 Stats")
            t2_runs = gr.Number(label="Runs Scored")
            t2_overs = gr.Number(label="Overs Faced (If All Out, enter total match overs)")
            
    calc_btn = gr.Button("Calculate NRR", variant="primary")
    
    with gr.Row():
        t1_result = gr.Textbox(label="Result Team 1")
        t2_result = gr.Textbox(label="Result Team 2")

    calc_btn.click(
        fn=calculate_nrr, 
        inputs=[team1_input, team2_input, total_match_overs, t1_runs, t1_overs, t2_runs, t2_overs],
        outputs=[t1_result, t2_result]
    )

demo.launch()