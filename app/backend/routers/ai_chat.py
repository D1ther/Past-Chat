from flask import (
    request,
    jsonify
)

from app.backend.ai.responses import (
    generate_ai_answer
)

from app.backend.db.db_requests import (
    get_person_by_id
)

from app import (
    app
)

@app.get('/api/v1.0/chat/<int:person_id>')
def chat_with_ai_api(person_id):
    data = request.get_json()

    system_prompt = get_person_by_id(person_id=person_id).prompt
    user_prompt = data['user_prompt']

    return jsonify({'message':generate_ai_answer(system_prompt=system_prompt, user_prompt=user_prompt)}), 200

