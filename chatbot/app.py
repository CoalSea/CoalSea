import pandas as pd
import spacy
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load CSV
data = pd.read_csv('verizon_questions_and_answers.csv', encoding='latin1')
qa_pairs = {}
for index, row in data.iterrows():
    question = row['Questions']
    answer = row['Answers']
    link = row['Hyperlink']
    qa_pairs[question] = {'answer': answer, 'link': link}

# Spacy pipeline
nlp = spacy.load('en_core_web_sm')
SIMILARITY_THRESHOLD = 0.5

def lemmatize_text(text):
    doc = nlp(text)
    text = ' '.join([token.lemma_ for token in doc if not token.is_stop])
    return text

def chatbot_response(user_question):
    user_question = lemmatize_text(user_question)
    user_doc = nlp(user_question)

    for question, data in qa_pairs.items():
        question = lemmatize_text(question)
        question_doc = nlp(question)

        if user_doc.similarity(question_doc) > SIMILARITY_THRESHOLD:
            answer = data['answer']
            link = data['link']
            return f"{answer}\nFor more info please visit our Verizon Link at: {link}"

    return "I'm sorry, I don't have information on that topic. However, you can reach out to us at: https://www.verizon.com/support/contact-us"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.form['user_input']
    response = chatbot_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run()
