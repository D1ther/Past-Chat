from flask import (
    render_template
)

import requests

from app import (
    app,
    API_URL
)

@app.route('/')
def default():
    persons_response = requests.get(f'{API_URL}/get_all_persons')

    if persons_response.status_code == 200:
        persons = persons_response.json()

        return render_template('show_persons.html', persons=persons)
    else:
        return render_template('show_persons.html')