import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from pdf_processing import extract_text_from_pdf
from retrieval_system import create_embedding, index

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Extract text from PDF and create embedding
        text = extract_text_from_pdf(filepath)
        embedding = create_embedding(text)
        
        # Add the embedding to the FAISS index
        index.add(embedding)
        
        return jsonify({"message": "File uploaded and processed"}), 200

@app.route('/')
def hello_world():
    return 'Hello, RAG App!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
