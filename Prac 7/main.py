from flask import Flask, request, render_template, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
import models

app = Flask(__name__)
CORS(app, support_credentials=True)

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
    name = str(data["name"])
    price = float(data["price"])
    res = models.create_product(name, price)
    return str(res)


@app.route('/', methods=['PUT'])
def update_record():
    ''' UPDATE '''
    data = request.get_json()
    _id = int(data["id"])
    name = data["name"]
    price = float(data["price"])
    res = models.update_product(_id, name, price)
    return jsonify(res)


@app.route('/', methods=['DELETE'])
def delete_record():
    ''' DELETE '''
    data = request.get_json()
    _id = int(data["id"])
    #print(data)
    res = models.delete_product(_id)
    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True)