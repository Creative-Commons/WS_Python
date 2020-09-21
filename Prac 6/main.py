from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
import models
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prac6.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get_friend", methods=["POST"])
def get_friend():

    friend = models.get_friend()
    x = []
    friend = json.loads(friend)

    for y in friend.values():
        x.append(y)
    print(x)   
    return render_template("result.html", result = x)


if __name__ == "__main__":
    app.run(host = "localhost", port = 5000, debug = True)