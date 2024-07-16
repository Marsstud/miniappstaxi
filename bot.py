from flask import Flask, request
import requests

app = Flask(__name__)
TELEGRAM_API_URL = f'https://api.telegram.org/bot<6890315927:AAG8WeABGQlW9ot6rjC2qUBq7YGzpC4zTC8>/'

def send_message(chat_id, text):
    url = TELEGRAM_API_URL + 'sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    requests.post(url, json=payload)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message']['text']
        send_message(chat_id, f'Вы сказали: {text}')
    elif 'web_app_data' in data:
        chat_id = data['web_app_data']['user']['id']
        web_app_data = data['web_app_data']['data']
        send_message(chat_id, f'Получены данные с веб-приложения: {web_app_data}')
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True)
