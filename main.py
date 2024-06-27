from flask import Flask, request, jsonify, send_from_directory, render_template
from transformers import pipeline
from googletrans import Translator
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# Specify the model explicitly
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data['question']
    pdf_text = data['pdfText']

    print("Question:", question)
    print("PDF Text:", pdf_text[:1000])  # Print the first 1000 characters for debugging

    # Answer the question based on the PDF text
    malayalam_question = translator.translate(question, src='ml', dest='en').text
    print("malayalam_qs:", malayalam_question)
    answer = qa_pipeline(question=malayalam_question, context=pdf_text)['answer']
    print("Answer:", answer)  # Debug print

    # Translate the answer to Malayalam
    malayalam_answer = translator.translate(answer, src='en', dest='ml').text
    print("Malayalam Answer:", malayalam_answer)  # Debug print

    return jsonify({'answer': malayalam_answer})

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    malayalam_text = data['malayalamText']

    # Translate Malayalam text to English
    english_translation = translator.translate(malayalam_text, src='ml', dest='en').text

    return jsonify({'translation': english_translation})

if __name__ == '__main__':
    app.run(debug=True)
