from dotenv import  load_dotenv
from openai  import OpenAI
import anthropic
from pydub.playback import play
from utills import handle_tool_call,artist
from config import GPT_MODEL,tools
from config import claude_system



openai = OpenAI()
claude = anthropic.Anthropic()

def call_gpt(history):
    # messages_gpt = [{"role": "system", "content": gpt_system}] + history[-1]
    # print('history', history)
    response = openai.chat.completions.create(model=GPT_MODEL, messages=history,tools=tools)
    image = None
    messages = history.copy()
    if response.choices[0].finish_reason=="tool_calls":
        message = response.choices[0].message
        response, city = handle_tool_call(message)
        messages.append(message)
        messages.append(response)
        image = artist(city)
        history.extend(messages)
        response = openai.chat.completions.create(model=GPT_MODEL, messages=history)
        
    reply = response.choices[0].message.content
    # history.append({"role":"assistant", "content":reply})

    # Comment out or delete the next line if you'd rather skip Audio for now..
    # talker_gpt(reply)

    return image, history, reply


def call_claude(history):
    # messages = []
    completion = claude.messages.create(
        model="claude-3-haiku-20240307",
        system=claude_system,  # Pass system prompt here
        messages=history,
        max_tokens=500
    )

    message = completion.content[0].text
    # history.append({"role": "assistant", "content": message})

    # talker_claude(message)

    return message





def conversation(gpt_history,claude_history):


    image,gpt_history,gpt_next = call_gpt(gpt_history)
    gpt_history.append({'role':'assistant', 'content':gpt_next})
    claude_history.append({'role':'user', 'content':gpt_next})


    claude_next = call_claude(claude_history)
    gpt_history.append({'role':'user', 'content':claude_next})
    claude_history.append({'role':'assistant', 'content':claude_next})
    return gpt_history,claude_history,gpt_next,claude_next,image





