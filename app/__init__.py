from flask import Flask
from flask_socketio import SocketIO
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__,
            template_folder='frontend/templates',
            static_folder='frontend/static')

socketio = SocketIO(app)

app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default_secret_key')

AI_API_KEY = os.getenv('AI_API_KEY')
API_URL = os.getenv('API_URL')

from app.frontend.routers import *
from app.backend.routers import *
from app.frontend.sockets import *

def main():
    app.run(port=5000, host='0.0.0.0', debug=True)

@socketio.on('message')
def handle_message(data):
    print('Received message:', data)
    socketio.send(data, broadcast=True)

if __name__ == '__main__':
    main()
