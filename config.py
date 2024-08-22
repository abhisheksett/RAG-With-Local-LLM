import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MODEL_GPT = "gpt-3.5-turbo"
MODEL_MIXTRAL = "mixtral:8x7b"
MODEL_LLAMA = "llama3.1"
# Configuration variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("MODEL", MODEL_LLAMA)