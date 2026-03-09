import gradio as gr
import random
import urllib.parse

def get_custom_html():
    return """
    <head>
        <meta property="og:title" content="Number Guessing Challenge" />
        <meta property="og:description" content="I am playing this game, come and test your luck!" />
        <meta property="og:type" content="website" />
    </head>
    """

def game_logic(mode, guess, state):
    try:
        guess = int(guess)
    except:
        return "Please enter a valid number!", state["score"], state["attempts_left"], "", gr.update(visible=False), gr.update(visible=False)

    if not state or state["attempts_left"] <= 0:
        return "Please initialize the game first!", 0, 0, "", gr.update(visible=False), gr.update(visible=False)

    target = random.randint(1, state["end"])
    state["attempts_left"] -= 1
    
    if guess == target:
        state["score"] += 1
        msg = f"<center>Correct! The number was {target}."
    else:
        msg = f"<center>Wrong! The number was {target}."

    if state["attempts_left"] == 0:
        score = state['score']
        total = state['total_attempts']
        post_text = f"I got {score} out of {total} in Number guessing Game. Made by plabon. Test your luck!"
        game_link = "https://your-username-space-name.hf.space"
        share_url = f"https://www.facebook.com/sharer/sharer.php?u={urllib.parse.quote(game_link)}&quote={urllib.parse.quote(post_text)}"
        
        result_display = f"<center><h3>Game Over! Final Score: {score} | Accuracy: {(score/total)*100:.0f}%</h3></center>"
        share_button_html = f'''
        <div style="text-align: center; margin-top: 1px;">
            <a href="{share_url}" target="_blank" rel="noopener" style="display:inline-block; padding:12px 24px; background-color:#1877F2; color:white; text-decoration:none; border-radius:8px; font-weight:bold; font-family:sans-serif;">
                Post to Facebook
            </a>
        </div>
        '''
        return msg, state["score"], state["attempts_left"], result_display, gr.update(visible=True), gr.update(value=share_button_html, visible=True)
    
    return msg, state["score"], state["attempts_left"], "", gr.update(visible=False), gr.update(visible=False)

def init_game(mode):
    settings = {'Easy': (10, 5), 'Medium': (15, 10), 'Hard': (20, 15)}
    end, attempts = settings.get(mode, (10, 5))
    range_hint = {"Easy": "1-10", "Medium": "1-15", "Hard": "1-20"}
    hint = f"<center><b>Type Between: {range_hint.get(mode)}</b></center>"
    
    # Initialize korar somoy share_area hide kora hoyeche
    return {"end": end, "total_attempts": attempts, "attempts_left": attempts, "score": 0}, attempts, 0, "<center>Game Initialized. Start guessing!", gr.update(visible=False), "", hint, gr.update(visible=False)



with gr.Blocks(head=get_custom_html(), theme=gr.themes.Default(primary_hue="blue")) as demo:
    state = gr.State({})
    gr.Markdown("# <center>Number Quest</center>")
    
    hint_display = gr.Markdown()
    result_display = gr.Markdown()
    
    with gr.Row():
        score_box = gr.Number(label="Score", interactive=False)
        attempts_box = gr.Number(label="Attempts Left", interactive=False)
    
    with gr.Column():
        mode_dropdown = gr.Dropdown(["Easy", "Medium", "Hard"], label="Select Mode", value="Easy")
        start_btn = gr.Button("Initialize Game", variant="primary")
    
    guess_input = gr.Textbox(label="Your Guess: ", placeholder="Enter your number here...", value="")
    submit_btn = gr.Button("Guess", variant="primary")
    output_msg = gr.Markdown("<center>Ready to play?</center>")
    
    share_area = gr.HTML(visible=False)

    # Output list-e 'share_area' add kora hoyeche jate button hide hoy
    start_btn.click(init_game, inputs=[mode_dropdown], outputs=[state, attempts_box, score_box, output_msg, start_btn, result_display, hint_display, share_area])
    submit_btn.click(game_logic, inputs=[mode_dropdown, guess_input, state], outputs=[output_msg, score_box, attempts_box, result_display, start_btn, share_area])

demo.launch()