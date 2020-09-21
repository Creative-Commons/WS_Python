from flask import Flask, request, render_template, redirect, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
import json
import models

app = Flask(__name__)

api = Api(app)
CORS(app, support_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prac7.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('price')

class ProductList(Resource):
    def get(self):
        results = models.get_products()
        products = []
        for r in results:
            products.append({
                "id": r.id,
                "name": r.name,
                "price": r.price
            })

        return {"products": products}

    def post(self):
        data = request.get_json()
        print(data)
        name = str(data["name"])
        price = float(data["price"])

        res = models.create_product(name, price)
        print(res)

        return str(res)


api.add_resource(ProductList, '/')

if __name__ == "__main__":
    app.run(debug=True)

'''
def home():
    products = models.get_products()
    return render_template("home.html", products = products)


def create_product():
    name = request.form["name"]
    price = request.form["price"]
    res = models.create_product(name, price)
    print(res)
    return redirect("/")

def delete_product():
    _id = request.form["id"]
    res = models.delete_product(_id)
    print(res)
    return redirect("/")

def update_product():
    _id = request.form["id"]
    name = request.form["name"]
    price = request.form["price"]
    res = models.update_product(_id, name, price)
    print(res)
    return redirect("/")
    
'''