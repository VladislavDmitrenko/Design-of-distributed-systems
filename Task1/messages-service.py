from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/messages', methods=['GET'])
def get_messages():
    message = "This is a static message from Messages Service"
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(port=8002, debug=True)