# app.py
from flask import Flask, render_template

app = Flask(__name__)

# Route principale
@app.route('/')
def index():
    return render_template("index.html", data="mohamed est un joli garcon")

# Lancer l'application Flask
if __name__ == '__main__':
    app.run(debug=True)
