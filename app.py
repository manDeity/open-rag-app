from flask import Flask, request, jsonify
from llm_integration import generate_text  # Import the generate_text function

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    response = generate_text(prompt)
    return jsonify({"response": response})

@app.route('/')
def hello_world():
    return 'Hello, RAG App!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
