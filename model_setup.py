from langchain_openai.chat_models import ChatOpenAI
from langchain_community.llms import Ollama
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import OllamaEmbeddings
from config import OPENAI_API_KEY, MODEL

# Global variables
model = None
embeddings = None

def setup_model():
    global model, embeddings
    if MODEL.startswith("gpt"):
        model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model=MODEL)
        embeddings = OpenAIEmbeddings()
    else:
        model = Ollama(model=MODEL)
        embeddings = OllamaEmbeddings(model=MODEL)

def get_embedding():
    return embeddings

def get_model():
     global model
     if model is None:
        setup_model()
     return model