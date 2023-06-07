from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []

@app.route('/log', methods=['POST'])
def log_message():
    message = request.json.get('message')

    # Save the message in memory
    messages.append(message)

    return jsonify({'success': True})

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

if __name__ == '__main__':
    app.run(port=8001, debug=True)