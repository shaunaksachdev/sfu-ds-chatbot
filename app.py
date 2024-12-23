# app.py

from flask import Flask, render_template, request, jsonify
from chatbot import process_query

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_query = data.get("query", "")
    response = process_query(user_query)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
