from flask import Flask, request, jsonify
# Створення інстанції Flask:
app = Flask(__name__)
# Оголошення змінної messages:
messages = []

# Визначення маршрутів та функцій-обробників:
@app.route('/log', methods=['POST'])
def log_message():
    message = request.json.get('message')

    # Save the message in memory
    messages.append(message)

    return jsonify({'success': True})

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)
# Запуск сервера:
if __name__ == '__main__':
    app.run(port=8001, debug=True)