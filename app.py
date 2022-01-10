
'''
Source:

Author: 
    Raja CSP
    Elaika VM
'''
from flask import Flask,render_template, jsonify, request
import random
import json

app  = Flask(__name__)
PORT = 4538

@app.route("/", methods = ["GET"])
def home_page():
    
    return render_template("static.html") 

if __name__ == "__main__":
    app.run(
        debug = True, 
        host = "0.0.0.0", 
        port = PORT
    )