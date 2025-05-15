# Summarizing Customer-Agent Chat History Using LLMs

This project demonstrates how Large Language Models (LLMs), such as GPT-4, can be used to summarize multi-turn chat conversations between customers and support agents. This approach is inspired by a production use case implemented at GEICO.

## 🧠 Problem Statement
Customer-agent transcripts are often lengthy and hard to scan quickly. Support agents and analysts need a concise summary of the conversation, including:
- The customer’s issue
- Tone/sentiment
- Final resolution (if any)

## 💡 Solution
We use LLM-based summarization via prompt engineering to generate clear summaries that improve:
- Agent handoff speed
- Quality control
- Escalation routing

## 📁 Project Structure
```plaintext
├── data/ # Sample mock chat logs 
├── notebooks/ # Jupyter notebook for step-by-step demo
├── prompts/ # Prompt versions used for comparison
├── src/ # Modular Python code 
├── slides/ # Presentation deck 
├── outputs/ # Generated summaries 
├── requirements.txt # Dependencies
```


## 🚀 Technologies
- OpenAI GPT-4 (via API)
- Python 3.9+
- Pandas, dotenv
- Prompt engineering techniques

## 🔍 Try It
Run the notebook in `/notebooks` to compare prompt results.

## 📬 Contact
Created by Marwah Faraj – inspired by real use cases in customer experience automation.
