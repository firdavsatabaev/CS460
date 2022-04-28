import sqlite3
import requests
from flask import Flask, jsonify, render_template
from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__, template_folder='templates')



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/api/digits/", methods=['POST'])
def digitsV():

    return 1











if __name__ == "__main__":
    app.debug = True
    app.run()