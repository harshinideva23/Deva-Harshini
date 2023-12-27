from flask import Flask, request, jsonify, session
import json
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

# Sample questions (you can replace these with your own)
questions = [
    {'id': 1, 'question': 'What is the capital of France?', 'difficulty': 2},
    {'id': 2, 'question': 'Translate "Hello" to Spanish.', 'difficulty': 1},
    # Add more questions here
]

# Sample user data (for demonstration purposes)
users = {}


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate input (add more validation as needed)

    # Save user data in session (for simplicity, you might want to use a database)
    session['username'] = username

    return jsonify({'message': 'Registration successful'})


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate input (add more validation as needed)

    # Save user data in session (for simplicity, you might want to use a database)
    session['username'] = username

    return jsonify({'message': 'Login successful'})


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'Logout successful'})


@app.route('/get_question', methods=['GET'])
def get_question():
    # Get user proficiency level (for simplicity, proficiency is hardcoded)
    proficiency_level = 3

    # Filter questions based on proficiency level
    filtered_questions = [q for q in questions if q['difficulty'] <= proficiency_level]

    # Randomly select a question from filtered questions
    selected_question = random.choice(filtered_questions)

    return jsonify(selected_question)


@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    data = request.get_json()
    user_answer = data.get('answer')
    question_id = data.get('question_id')

    # Check the correctness of the answer (add more logic as needed)

    # Update user progress (for simplicity, progress is not tracked in this example)

    return jsonify({'message': 'Answer submitted successfully'})


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
