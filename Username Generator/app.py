import gradio as gr

def generate_usernames(first_name, last_name):
    f = first_name.lower().strip()
    l = last_name.lower().strip()
    if not f or not l: return "<div>Please enter names</div>"
    
    usernames = [f+l, l+f, f+"123", l+"123", f+l+"123", "im-"+f, f+l+"69", f+"_"+l, f+"."+l, l+"."+f]
    
    html = "<div style='display: flex; flex-direction: column; gap: 5px;'>"
    for u in usernames:
        # প্রতিটি নামের পাশে একটি বাটন যা ক্লিপবোর্ডে কপি করবে
        html += f"""
        <div style='padding: 5px; background: #4f46e5; border: 1px solid #ddd; border-radius: 5px; display: flex; justify-content: space-between; align-items: center;'>
            <span>{u}</span>
            <button onclick="navigator.clipboard.writeText('{u}')" style='cursor: pointer;'>Copy</button>
        </div>
        """
    html += "</div>"
    return html

with gr.Blocks() as demo:
    gr.Markdown("# Username Generator")
    with gr.Row():
        f_input = gr.Textbox(label="First Name")
        l_input = gr.Textbox(label="Last Name")
    
    btn = gr.Button("Generate Usernames", variant="primary")
    output = gr.HTML()
    
    btn.click(fn=generate_usernames, inputs=[f_input, l_input], outputs=output)

demo.launch(theme=gr.themes.Soft())