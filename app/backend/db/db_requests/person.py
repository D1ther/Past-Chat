from flask import (
    jsonify
)

from app.backend.db.base import (
    Session
)

from app.backend.db.models import (
    Person
)

def add_new_person(name, description, prompt, avatar):
    with Session() as session:
        person = session.query(Person).where(Person.name == name).one_or_none()

        if person:
            return jsonify({'message': 'Person with this name already exists'}), 400
        else:
            person = Person(name=name, description=description, prompt=prompt, avatar=avatar)
            session.add(person)
            session.commit()

            return jsonify({'message': 'Person added successfully'}), 200