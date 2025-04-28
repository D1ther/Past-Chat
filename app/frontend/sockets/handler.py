from flask import (
    session
)

from flask_socketio import (
    emit
)

from app import (
    socketio,
    API_URL
)

import requests

@socketio.on('send_message')
def handle_message(data):
    person_id = data['person_id']
    user_message = data['message']

    session['chat_history'] = []
    
    session['chat_history'].append({'role': 'user', 'text': user_message})
    
    chat_response = requests.get(f'{API_URL}/chat/{person_id}', json={'user_prompt': user_message})
    
    if chat_response.status_code == 200:
        ai_message = chat_response.json().get('message', 'Помилка відповіді AI')
    else:
        ai_message = 'AI не зміг відповісти'

    session['chat_history'].append({'role': 'ai', 'text': ai_message})
    
    emit('receive_message', {'role': 'ai', 'text': ai_message})