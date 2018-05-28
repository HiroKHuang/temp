from simpledu.app import create_app
from simpledu.models import db, Course, User

app = create_app('development')

if __name__ == '__main__':
    db.create_all()
    user = User(username='admin')
    course1 = Course(name='python course', author=user)
    course2 = Course(name='flask course', author=user)
    db.session.add_all([user,course1,course2])
    db.session.commit()
    app.run()
