import json
import openai
import os
from src.utils import load_api_key

def load_chat(chat_path):
    with open(chat_path, "r") as f:
        chat = json.load(f)
    return chat

def format_chat(chat_data):
    return "\n".join([f"{msg['sender'].capitalize()}: {msg['text']}" for msg in chat_data["messages"]])

def load_prompt(template_path, chat_text):
    with open(template_path, "r") as f:
        prompt_template = f.read()
    return prompt_template.replace("{chat_messages}", chat_text)

def generate_summary(prompt, model="gpt-4", temperature=0.3):
    openai.api_key = load_api_key()
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=400
    )
    return response.choices[0].message["content"]

if __name__ == "__main__":
    chat = load_chat("data/sample_chat_1.json")
    chat_text = format_chat(chat)

    prompt = load_prompt("prompts/refined_prompt.txt", chat_text)
    summary = generate_summary(prompt)
    print("\n--- Generated Summary ---\n")
    print(summary)
