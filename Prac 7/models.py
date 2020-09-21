from main import db
from sqlalchemy.exc import IntegrityError


class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True, nullable = False)
    price = db.Column(db.Integer, nullable = False)

db.create_all()


def create_product(name, price):
    P = Product(name = name, price = price)
    try:
        db.session.add(P)
        db.session.commit()
        return True
    except IntegrityError:
        db.session.rollback()
        return False

def delete_product(_id):
    P = db.session.query(Product).filter_by(id = _id).first()
    try:
        db.session.delete(P)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False

def update_product(_id, name, price):
    P = db.session.query(Product).filter_by(id = _id).first()
    P.name = name
    P.price = price
    try:
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False

def get_products():
    products = db.session.query(Product).all()
    return products