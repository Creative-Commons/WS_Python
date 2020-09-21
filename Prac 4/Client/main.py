from flask import Flask, render_template, request
from zeep import Client

url = 'http://localhost:44308/Operation.asmx?WSDL'
client = Client(url)


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add", methods=["POST"])
def add():
    num1 = int(request.form["num1"])
    num2 = int(request.form["num2"])
    result = client.service.Add(num1, num2)
    return "Sum: " + str(result)

@app.route("/multiply", methods=["POST"])
def multiply():
    num1 = int(request.form["num1"])
    num2 = int(request.form["num2"])
    result = client.service.Multiply(num1, num2)
    return "Product: " + str(result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)