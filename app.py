from utills import talker_claude,talker_gpt
from llms_agents import conversation
import gradio as gr
from config import gpt_system



def start_conv():
    chat = []
    final_image = None
    gpt_history = [{"role": "system", "content": gpt_system}]
    claude_history = []
    for i in range(4):
        gpt_history,claude_history ,gpt_next,claude_next,image = conversation(gpt_history,claude_history)
        gpt_history.append({'role':'assistant', 'content':gpt_next})
        claude_history.append({'role':'user', 'content':gpt_next})

        chat.append((None, f"🤖 GPT: {gpt_next}"))
        yield chat, final_image if final_image else gr.update()
        talker_gpt(gpt_next)


        gpt_history.append({'role':'user', 'content':claude_next})
        claude_history.append({'role':'assistant', 'content':claude_next})

        
        chat.append((f"🧑 Claude: {claude_next}", None))
        yield chat, final_image if final_image else gr.update()
        talker_claude(claude_next)

        if image:
            final_image = image.copy()
            yield chat, final_image




with gr.Blocks() as demo:
    gr.Markdown("## 🎙️ Claude & GPT Travel Chat")

    start_btn = gr.Button("Start Chat")
    chatbox = gr.Chatbot()
    image_output = gr.Image(label="Generated Image", type="pil",height=500)
    start_btn.click(fn=start_conv, inputs=[], outputs=[chatbox, image_output])

    
demo.launch()