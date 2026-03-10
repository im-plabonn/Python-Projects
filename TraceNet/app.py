import speedtest
import gradio as gr
from datetime import datetime

def check_speed():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        d_speed = st.download() / 1_000_000
        u_speed = st.upload() / 1_000_000
        ping = st.results.ping
        today = datetime.now().strftime("%d %B, %Y (%I:%M %p)")
        return round(d_speed, 2), round(u_speed, 2), round(ping, 1), today
    except Exception as e:
        return 0, 0, 0, f"Error: {str(e)}"

# Custom CSS to center text and labels
custom_css = """
input {text-align: center !important;}
label {text-align: center !important; width: 100% !important; justify-content: center !important;}
span {text-align: center !important; width: 100% !important;}
"""

with gr.Blocks(theme=gr.themes.Soft(), css=custom_css) as demo:
    gr.Markdown("<h1 style='text-align: center;'>TraceNet</h1>")
    gr.Markdown("<p style='text-align: center;'>Click the button below to test your real-time network performance.</p>")
    
    with gr.Row():
        download_display = gr.Number(label="Download (Mbps)", value=0, precision=2)
        upload_display = gr.Number(label="Upload (Mbps)", value=0, precision=2)
        ping_display = gr.Number(label="Ping (ms)", value=0, precision=1)
        
    with gr.Row():
        last_run = gr.Textbox(label="Last Test Time", placeholder="Not tested yet", interactive=False)
        
    start_btn = gr.Button("Run Speed Test", variant="primary")
    
    start_btn.click(
        fn=check_speed,
        inputs=None,
        outputs=[download_display, upload_display, ping_display, last_run]
    )

if __name__ == "__main__":
    demo.launch()