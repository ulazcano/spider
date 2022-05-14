# Libraries
import matplotlib.pyplot as plt, mpld3
import pandas as pd
from math import pi
import base64
from io import BytesIO
from flask import Flask, render_template, request
from matplotlib.figure import Figures

app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html')


@app.route('/',methods = ['GET'])
def show_index_html():
        return render_template("index.html")

@app.route('/send_data', methods = ['POST'])
def get_data_from_html():
        pay = request.form['pay']
        print ("Pay is " + pay)
        #return "Data sent. Please check your program log"
        return render_template("index.html")

if __name__ == '__main__':
        app.run(debug=True)


