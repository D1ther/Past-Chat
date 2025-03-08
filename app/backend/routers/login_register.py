from flask import (
    jsonify,
    request
)

from app.backend.db.db_requests import (
    register_user,
    login_user
)

from app import (
    app
)

import base64

@app.post('/api/v1.0/register')
def register_user_api():
    data = request.get_json()

    name = data['name']
    email = data['email']
    password = data['password']
    avatar = base64.b64decode(data['avatar'])

    return register_user(name, email, password, avatar)

@app.post('/api/v1.0/login')
def login_user_api():
    data = request.get_json()

    email = data['email']
    password = data['password']

    return login_user(email, password)