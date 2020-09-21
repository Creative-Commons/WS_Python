from main import db
from sqlalchemy.exc import IntegrityError


class Friend(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30))

db.create_all()


def insert_friend(_id, name):
    F = Friend(id = _id, first_name = name)
    try:
        db.session.add(F)
        db.session.commit()
        print(F, "inserted")
        return True
    except IntegrityError:
        db.session.rollback()
        return False


def get_friend_from_id(_id):
    friend = db.session.query(Friend).filter_by(id = _id).first()
    print(friend)
    return friend