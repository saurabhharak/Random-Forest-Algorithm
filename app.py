from flask import Flask, request,render_template
import random
import string
import os
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("url_page.html")


@app.route('/predi/',methods=['POST','GET'] )
def home1():
    if request.method == 'POST':
        variance = request.form["variance"]
        skewness = request.form["skewness"]
        curtosis = request.form["curtosis"]
        entropy = request.form["entropy"]
        pickle_in = open('classifier.pkl','rb')
        classifier = pickle.load(pickle_in)
        prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
     
        return render_template("url_page.html",outputt = "The Predicated Value is ${}".format(prediction))
     
    else:
        return render_template("url_page.html")

if __name__ == '__main__':
    app.run(debug=True)
