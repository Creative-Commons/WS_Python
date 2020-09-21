from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/f_c", methods=["POST"])
def f_c():
    num1 = float(request.form["num1"])
    return "fahrenheit to celsius: " + str(((num1 - 32) * (5 / 9)))

@app.route("/c_f", methods=["POST"])
def c_f():
    num1 = float(request.form["num1"])
    return "celsius to fahrenheit: " + str((num1*(9/5) + 32))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
    
    
          