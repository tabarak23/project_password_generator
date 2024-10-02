from flask import Flask, request, jsonify, render_template
import string
import random

app = Flask(__name__)

def generate_password(length):
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")

    password_chars = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    remaining_length = length - 4
    password_chars += random.choices(all_chars, k=remaining_length)

    random.shuffle(password_chars)
    return ''.join(password_chars)

@app.route('/')
def index():
    return render_template('index.html')  # Serve the index.html page

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    length = data.get('length')

    if not length or length < 4:
        return jsonify({'error': 'Length must be at least 4'}), 400

    password = generate_password(length)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
