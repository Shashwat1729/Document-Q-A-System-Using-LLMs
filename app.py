from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from model import answer_question
from utils.file_parser import extract_text_from_file

app = Flask(__name__)

# Set the folder for uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Extract text from the uploaded file
        text = extract_text_from_file(file_path)
        return render_template('index.html', file_text=text, filename=filename)

@app.route('/ask', methods=['POST'])
def ask_question():
    question = request.form['question']
    document_text = request.form['document_text']
    
    if not question or not document_text:
        return redirect(url_for('index'))
    
    # Generate the answer using the model
    answer = answer_question(question, document_text)
    return render_template('index.html', question=question, answer=answer, file_text=document_text)

if __name__ == '__main__':
    app.run(debug=True)
