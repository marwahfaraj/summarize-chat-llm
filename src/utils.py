import os
from dotenv import load_dotenv

def load_api_key():
    """
    Load the OpenAI API key from a .env file.
    """
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file.")
    return api_key
