from main import db
from sqlalchemy.exc import IntegrityError
import json

class Friend(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30))

db.create_all()


for i in ['Ram', 'Sham', 'Jaisal']:
    x = db.session.query(Friend).filter_by(first_name = i).first()
    if not x:
        F = Friend(first_name = i)
        db.session.add(F)
        db.session.commit()
        print(F, ' inserted')
    else:
        db.session.rollback()
        print(i, 'exists')


def get_friend():
    friend = db.session.query(Friend).all()
    d = {}; i = 0
    for x in friend:
        d[i] = x.first_name
        i += 1
    print(friend)
    return json.dumps(d)