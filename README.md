# RAG With Local LLM

This is a simple RAG based application which loads a pdf and anble to answer questions based on the data provided.

## Prerequisites

### Setting Up a Virtual Environment

Follow these steps to create and activate a virtual environment for your Python project:

1. **Open the terminal in Visual Studio Code.**

2. **Navigate to your project directory:**

   ```sh
   cd /path/to/your/project
   ```

3. Create a virtual environment:
    ```
    python3 -m venv venv
    ```

4. Activate the virtual environment:
    ```
    source venv/bin/activate
    ```

5. (Optional) Install your project dependencies:
    ```
    pip install -r requirements.txt
    ```

#### Deactivating the Virtual Environment

To deactivate the virtual environment, simply run:
    ```
    deactivate
    ```

#### Additional Information
- Ensure you have Python 3 installed on your machine.
- You can add more dependencies to ```requirements.txt``` and install them using:

    ```
    pip install -r requirements.txt
    ```

Your virtual environment is now set up and activated.


## Create environment file

Create a .env file at project root and create a key OPENAI_API_KEY = <your_openai_key>.

## Install Ollama

Ollama can be installed locally from <a href="https://ollama.com/download">here</a>.

To run a llama model in local, execute:
    ```
    ollama run llama3.1
    ```

## Get Pinecone API key

Create an account in pinecone and get the api key. Add the key in .env file:
PINECONE_API_KEY = <api_key>.

### How to run

Just run ```python3 main.py```

If you need to change the question, update QUESTION_TEXT value in main.py file.