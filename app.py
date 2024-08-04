from openai import OpenAI
from flask import Flask, request, render_template, jsonify
import os

app = Flask(__name__)

# Ensure you have set up your OpenAI API key
# Replace 'your-api-key' with your actual OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/qna', methods=['POST'])
def qna():
    data = request.get_json()
    pertanyaan = data['pertanyaan']
    
    # Call OpenAI API with the question
    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {
                'role': 'user',
                'content': pertanyaan
            }
        ]
    )

    jawaban = response.choices[0].message.content
    
    return jsonify({'jawaban': jawaban})

if __name__ == "__main__":
    app.run(debug=True)
