from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Разрешаем CORS для подключения с внешней панели

@app.route('/command', methods=['POST'])
def receive_command():
    data = request.get_json()
    command = data.get('command')
    
    # Логика обработки команд
    if command == 'open_gate':
        response = "Ворота открыты"
    elif command == 'close_gate':
        response = "Ворота закрыты"
    elif command == 'close_windows':
        response = "Окна закрыты"
    elif command == 'lower_house':
        response = "Дом убран под землю"
    elif command == 'sos':
        response = "SOS! Уведомление отправлено"
    else:
        response = "Неизвестная команда"
    
    print(f"Получена команда: {command}")
    return jsonify({"status": response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
