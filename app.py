from flask import Flask, app, request
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return'Funcionó'

if __name__=='__name__':
    app.run()
