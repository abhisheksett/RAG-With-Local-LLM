from langchain.prompts import PromptTemplate

def setup_prompt(context, question):
    template = """
    Answer the question based on the context below. If you don't know the answer, reply "I don't know".

    Context: {context}

    Question: {question}
    """
    prompt = PromptTemplate.from_template(template)
    prompt.format(context=context, question=question)
    return prompt