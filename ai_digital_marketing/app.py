from flask import Flask, render_template, request, jsonify
from model import find_customers_by_interest

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():

    user_message = request.json['message']

    response = find_customers_by_interest(user_message)

    return jsonify({'reply': response})


if __name__ == '__main__':
    app.run(debug=True)