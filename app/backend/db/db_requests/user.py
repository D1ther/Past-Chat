from flask import (
    jsonify
)

from app.backend.db.base import (
    Session
)

from app.backend.db.models import (
    User
)

def register_user(name, email, password, avatar):
    with Session() as session:
        user = session.query(User).where(User.email == email).one_or_none()

        if user:
            return jsonify({'message':'User arledy exists'}), 400
        else:
            user = User(name=name, email=email, password=password, avatar=avatar)
            user.hash_password()

            session.add(user)
            session.commit()

            return jsonify({'message':'User created'}), 200
        
def login_user(email, password):
    with Session() as session:
        user = session.query(User).where(User.email == email).one_or_none()

        if user:
            if user.check_password(password):
                return jsonify({'message':'Login success'}), 200
            else:
                return jsonify({'message':'Incorrect password'}), 400
        else:
            return jsonify({'message':'User not found'}), 400
