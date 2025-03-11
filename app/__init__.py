from flask import (
    Flask
)

from dotenv import (
    load_dotenv
)

import os

load_dotenv()

app = Flask(__name__,
            template_folder='frontend/templates',
            static_folder='frontend/static')

AI_API_KEY = os.getenv('AI_API_KEY')
API_URL = os.getenv('API_URL')

from app.frontend.routers import *
from app.backend.routers import *

def main():
    app.run(port=5000, host='0.0.0.0', debug=True)