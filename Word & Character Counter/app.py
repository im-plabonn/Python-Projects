import gradio as gr

def analyze_text(text):
    words = len(text.split())
    characters = len(text)
    upper = sum(1 for char in text if char.isupper())
    lower = sum(1 for char in text if char.islower())
    space = text.count(" ")
    
    return words, characters, upper, lower, space

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Text Analyzer Tool")
    gr.Markdown("Paste your text below to get an instant analysis of your content.")
    
    with gr.Row():
        input_text = gr.Textbox(lines=6, label="Input Text", placeholder="Paste your text here...")
    
    analyze_btn = gr.Button("Analyze Text", variant="primary")
    
    with gr.Row():
        w_out = gr.Number(label="Words")
        c_out = gr.Number(label="Characters")
        u_out = gr.Number(label="Uppercase")
        l_out = gr.Number(label="Lowercase")
        s_out = gr.Number(label="Spaces")
        
    analyze_btn.click(
        fn=analyze_text,
        inputs=input_text,
        outputs=[w_out, c_out, u_out, l_out, s_out]
    )

if __name__ == "__main__":
    demo.launch()