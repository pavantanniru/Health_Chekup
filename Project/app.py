from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route("/base")

def base():
    return render_template("Base.html")

@app.route("/diab")

def dia():
    return render_template("diabetes.html")


if __name__ == '__main__':
    app.run(debug=True)
