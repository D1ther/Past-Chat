from flask import (
    Flask
)

from flask_socketio import (
    SocketIO
)

from dotenv import (
    load_dotenv
)

from flask_cors import (
    CORS
)

import os

load_dotenv()

app = Flask(__name__,
            template_folder='frontend/templates',
            static_folder='frontend/static')
app.secret_key = 'daondawjdoawdjawiod'
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
CORS(app=app)

socketio = SocketIO(app, async_mode='threading', cors_allowed_origins='*')

app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default_secret_key')

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
API_URL = os.getenv('API_URL')

from app.frontend.routers import *
from app.backend.routers import *
from app.frontend.sockets import *

def main():
    socketio.run(app, port=5000, host='127.0.0.1', debug=True)

@socketio.on('message')
def handle_message(data):
    print('Received message:', data)
    socketio.send(data, broadcast=True)
