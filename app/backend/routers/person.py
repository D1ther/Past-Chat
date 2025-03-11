from flask import (
    request
)

from app.backend.db.db_requests import (
    add_new_person,
    get_all_persons
)

from app import (
    app
)

import base64

@app.post('/api/v1.0/add_person')
def add_person_api():
    data = request.get_json()

    name = data['name']
    description = data['description']
    prompt = data['prompt']
    avatar = base64.b64decode(data['avatar'])

    return add_new_person(name, description, prompt, avatar)

@app.get('/api/v1.0/get_all_persons')
def get_all_persons_api():
    return get_all_persons(), 200
