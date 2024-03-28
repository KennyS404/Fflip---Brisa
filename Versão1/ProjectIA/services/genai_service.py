import google.generativeai as genai
from utils.env_loader import get_api_key

def configure_genai():
    api_key = get_api_key()
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")
    return model
