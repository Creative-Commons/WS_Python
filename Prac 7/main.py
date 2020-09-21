from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import models


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prac7.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.route("/")
def home():
    products = models.get_products()
    return render_template("home.html", products = products)

@app.route("/create_product", methods=["POST"])
def create_product():
    name = request.form["name"]
    price = request.form["price"]
    res = models.create_product(name, price)
    print(res)
    return redirect("/")

@app.route("/delete_product", methods=["POST"])
def delete_product():
    _id = request.form["id"]
    res = models.delete_product(_id)
    print(res)
    return redirect("/")

@app.route("/update_product", methods=["POST"])
def update_product():
    _id = request.form["id"]
    name = request.form["name"]
    price = request.form["price"]
    res = models.update_product(_id, name, price)
    print(res)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)