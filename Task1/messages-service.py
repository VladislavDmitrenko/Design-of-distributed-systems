from flask import Flask, jsonify
# Створення інстанції Flask:
app = Flask(__name__)

# Визначення маршруту та функції-обробника:
@app.route('/messages', methods=['GET'])
def get_messages():
    message = "This is a static message from Messages Service"
    return jsonify({'message': message})
# Запуск сервера:
if __name__ == '__main__':
    app.run(port=8002, debug=True)