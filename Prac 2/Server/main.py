from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
import models

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prac2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/insert_friend", methods=["POST"])
def insert_friend():
    _id = request.form["id"]
    name = request.form["name"]
    result = models.insert_friend(_id, name)
    print(result)

    return redirect("/")


@app.route("/get_friend", methods=["POST"])
def get_friend():
    _id = request.form["id"]
    friend = models.get_friend_from_id(_id)
    friend_name = friend.first_name

    return render_template("result_page.html", result = friend_name)


if __name__ == "__main__":
    app.run(host = "localhost", port = 5000, debug = True)