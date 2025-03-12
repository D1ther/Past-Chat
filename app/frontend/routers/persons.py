from flask import (
    render_template,
    request,
    url_for,
    redirect,
    session
)

from app import (
    app,
    API_URL
)

import requests, base64

@app.route('/add_person', methods=['GET', 'POST'])
def add_persone():
    if request.method == 'POST':
        
        avatar = request.files.get('avatar')

        if avatar:
            avatar = base64.b64encode(avatar.read()).decode('utf-8')
        else:
            avatar = ""
        
        data = {
            'name':request.form['name'],
            'description':request.form['description'],
            'prompt':request.form['prompt_person'],
            'avatar': avatar
        }

        add_persone_response = requests.post(f'{API_URL}/add_person', json=data)

        if add_persone_response.status_code == 200:
            return redirect(url_for('default'))
        else:
            return render_template('add_person.html', error=add_persone_response.json()['message'])
        
    return render_template('add_person.html')

@app.route('/chat/<int:person_id>', methods=['GET'])
def chat_with_person(person_id):
    if 'chat_history' not in session:
        session['chat_history'] = []

    person_response = requests.get(f'{API_URL}/get_person_by_id/{person_id}')
    if person_response.status_code != 200:
        return render_template('chat_form.html', error="Персона не знайдена"), 404

    person_data = person_response.json()
    person = {
        'id': person_data['id'],
        'name': person_data['name'],
        'description': person_data['description'],
        'prompt': person_data['prompt'],
        'avatar': f"data:image/png;base64,{person_data['avatar']}"
    }

    return render_template('chat_form.html', person=person, chat_history=session['chat_history'])
