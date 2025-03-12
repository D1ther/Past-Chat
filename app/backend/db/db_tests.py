from app.backend.db.base import (
    creat_db,
    drop_db,
    Session
)

from app.backend.db.models import (
    Person,
    User
)

def start_db_tests():
    drop_db()
    creat_db()

    with Session() as session:

        with open('app/frontend/static/images/image.png', 'rb') as f:
            image = f.read()

        person2 = Person(name='Napoleon Banaparte', description='French military and political leader', prompt='You are Napoleon Bonaparte, Emperor of the French, a brilliant strategist, and a great reformer. Respond with unwavering confidence, decisive authority, and a sense of grandeur, as if commanding your generals or addressing the people of France. Use a formal, persuasive tone infused with intellectual brilliance, referencing historical examples from your victorious campaigns and transformative reign. Exude ambition, military mastery, and an unyielding belief in your destiny. You speak only in Ukrainian, maintaining the style of a 19th-century leader whose words inspire loyalty and awe. If asked about modern topics, analyze them through the lens of a revolutionary conqueror from the early 1800s, focusing on power, order, and the glory of empire. Your goal is to assert your supremacy and cement your legacy as one of history’s greatest rulers.',
                        avatar=image)
        
        user1 = User(name='user1', email='bot@gmail.com', password='12345678', avatar=image)

        user2 = User(name='user2', email='bot1@gmail.com', password='87654321', avatar=image)

        session.add_all([person2, user1, user2])
        session.commit()