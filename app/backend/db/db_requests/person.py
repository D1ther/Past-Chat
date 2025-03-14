from flask import (
    jsonify
)

from app.backend.db.base import (
    Session
)

from app.backend.db.models import (
    Person
)

import base64

def add_new_person(name, description, prompt, avatar):
    with Session() as session:
        person = session.query(Person).where(Person.name == name).one_or_none()

        if person:
            return jsonify({"message": "Персона з таким ім'ям вже існує в базі"}), 400
        else:
            person = Person(name=name, description=description, prompt=prompt, avatar=avatar)
            session.add(person)
            session.commit()

            return jsonify({'message': 'Person added successfully'}), 200
        
def get_person_by_id(person_id):
    with Session() as session:
        person = session.query(Person).where(Person.id == person_id).one_or_none()

        if person:
            return {
                'id': person.id,
                'name': person.name,
                'description': person.description,
                'prompt': person.prompt,
                'avatar': base64.b64encode(person.avatar).decode('utf-8')
            }
        else:
            return None
        
def get_all_persons():
    with Session() as session:
        
        persons = session.query(Person).all()

        return [person.to_dict() for person in persons]