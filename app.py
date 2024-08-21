from flask import Flask, request, jsonify
from llm_integration import generate_text
from retrieval_system import search_index

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    
    # Retrieve relevant documents
    relevant_docs = search_index(prompt)
    
    # Combine retrieved docs with the prompt
    augmented_prompt = prompt + " ".join(relevant_docs)
    
    # Generate response
    response = generate_text(augmented_prompt)
    
    return jsonify({"response": response})

@app.route('/')
def hello_world():
    return 'Hello, RAG App!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
