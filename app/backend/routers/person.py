from flask import (
    request
)

from app.backend.db.db_requests import (
    add_new_person,
    get_all_persons,
    get_person_by_id
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

@app.get('/api/v1.0/get_person_by_id/<int:person_id>')
def get_person_by_id_api(person_id):
    return get_person_by_id(person_id), 200

@app.get('/api/v1.0/get_all_persons')
def get_all_persons_api():
    return get_all_persons(), 200
