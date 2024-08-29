# open-rag-app
This repo is supposed to be an opensource Rag app

app.py : is the flask app with LLM dependencies

llm_integration.py: code to load the LLM model

retrieval_system.py : code to process documents and store their embeddings in FAISS

A Procfile is needed to tell Heroku how to run your application.

runtime.txt : Specify the Python version your app uses by creating a runtime.txt file in your repository
