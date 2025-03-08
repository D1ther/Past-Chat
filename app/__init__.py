from flask import (
    Flask
)

app = Flask(__name__,
            template_folder='frontend/templates',
            static_folder='frontend/static')

from app.frontend.routers import *
from app.backend.routers import *

def main():
    app.run(port=5000, host='0.0.0.0', debug=True)