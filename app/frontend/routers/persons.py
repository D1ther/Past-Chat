from flask import (
    render_template,
    request,
    url_for,
    redirect
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
