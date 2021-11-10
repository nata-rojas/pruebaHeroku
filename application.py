from flask import Flask, render_template
app = Flask(__name__)
datos = [{"nombre":"Luis", "edad":98}]
@app.route("/")
def index():
    return render_template("index.html", datos=datos)