from flask import Flask, request, render_template, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
import models

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prac7.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def query_records():
    ''' SELECT '''
    results = models.get_products()
    products = []
    for r in results:
        products.append({
            "id": r.id,
            "name": r.name,
            "price": r.price
        })

    return {"products": products}

@app.route('/', methods=['POST'])
def create_record():
    ''' CREATE '''
    data = request.get_json()
    print(data)
    name = str(data["name"])
    price = float(data["price"])

    res = models.create_product(name, price)
    print(res)

    return str(res)

@app.route('/', methods=['PUT'])
def update_record():
    ''' UPDATE '''
    data = request.get_json()
    print(data)
    return

@app.route('/', methods=['DELETE'])
def delete_record():
    ''' DELETE '''
    print(data)
    return


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