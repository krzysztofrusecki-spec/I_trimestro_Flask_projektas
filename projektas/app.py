from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/gameplay")
def gameplay():
    return render_template("gameplay.html")

@app.route("/history")
def history():
    return render_template("history.html")

@app.route("/tips")
def tips():
    return render_template("tips.html")

@app.route("/secret")
def secret():
    return render_template("secret.html")

if __name__ == "__main__":
    app.run(debug=True)
