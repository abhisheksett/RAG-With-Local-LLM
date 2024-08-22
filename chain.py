from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from prompt_setup import setup_prompt
from model_setup import get_model
from vector_store import get_vectorstore

# Global variable
parser = StrOutputParser()

def form_chain():
    model = get_model()
    retriever = None
    chain = (
        {
            "context": itemgetter("question") | retriever,
            "question": itemgetter("question"),
        }
        | setup_prompt
        | model
        | parser
    )
    return chain

def get_result(question):
    model = get_model()
    vectorstore = get_vectorstore()
    context = vectorstore.search(question, search_type="similarity", k=5)
    prompt = setup_prompt(context, question)
    
    formatted_prompt = prompt.format(context=context, question=question)

    # Process the chain
    if hasattr(model, 'generate'):
        chain_result = model.generate([formatted_prompt])
    else:
        chain_result = model(formatted_prompt)

    parsed_result = parser.parse(chain_result)
    answer_text = parsed_result.generations[0][0].text

    
    return answer_text