from flask import Flask, request, jsonify
import requests

# Створення інстанції Flask
app = Flask(__name__)
# Визначення URL-ів та адрес сервісів
logging_service_url = 'http://localhost:8000'
messages_service_url = 'http://localhost:8001'

# Визначення маршрутів та функцій-обробників
@app.route('/log', methods=['POST'])
def log_message():
    message = request.json.get('message')

    # Send the message to the Logging Service
    requests.post(logging_service_url + '/log', json={'message': message})

    return jsonify({'success': True})

@app.route('/messages', methods=['GET'])
# метод GET для отримання повідомлень.
def get_messages():
    # Get messages from the Messages Service
    response = requests.get(messages_service_url + '/messages')
    messages = response.json()

    return jsonify(messages)
# Запуск сервера
if __name__ == '__main__':
    app.run(port=8000, debug=True)


