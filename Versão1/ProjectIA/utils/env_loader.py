from dotenv import load_dotenv
import os

def get_api_key():
    load_dotenv()
    api_key = os.getenv('GOOGLE_API_KEY')
    if api_key is None:
        raise ValueError("A variável de ambiente 'GOOGLE_API_KEY' não está definida.")
    return api_key
