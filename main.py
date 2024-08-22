from config import MODEL
from model_setup import setup_model
from document_loader import load_pdf_and_split
from vector_store import store_in_vector_db, retrieve_from_vector_db
from chain import get_result

QUESTION_TEXT = "How Search Works?"

def initialize():
    setup_model()
    documents = load_pdf_and_split("data/seo-basics-mini-course.pdf")
    store_in_vector_db(documents)

def ask_question(question):
    # chain = form_chain()
    answer = get_result(question)
    return answer

if __name__ == "__main__":
    initialize()
    question = QUESTION_TEXT
    answer = ask_question(question)
    print(f"Answer: {answer}")
