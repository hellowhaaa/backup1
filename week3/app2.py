from flask import (Flask, redirect, url_for, session, render_template, 
                   request, flash, make_response, jsonify)

import forms
import models
from forms import SumUpForm
import json

DEBUG = True
LOCAL_HOST = ''

app = Flask(__name__)
app.secret_key = 'sdfjiohdgssdkghnlsdhildfs'

tpe = {
    "id": 0,
    "city_name": "Taipei",
    "country_name": "Taiwan",
    "is_capital": True,
    "location": {
        "longitude": 121.569649,
        "latitude": 25.036786
    }
}
nyc = {
    "id": 1,
    "city_name": "New York",
    "country_name": "United States",
    "is_capital": False,
    "location": {
        "longitude": -74.004364,
        "latitude": 40.710405
    }
}
ldn = {
    "id": 2,
    "city_name": "London",
    "country_name": "United Kingdom",
    "is_capital": True,
    "location": {
        "longitude": -0.114089,
        "latitude": 51.507497
    }
}
cities = [tpe, nyc, ldn]

@app.route('/')
def index():
    word = 'Hello, My Server'

    return render_template('first_page.html', word=word)


@app.route('/data', methods=['GET'])
def data():
    number = request.args.get('number')
    if not number:
        number = 'Lack of Parameter'
    elif number.isalpha():
        number = 'Wrong Parameter'
    else:
        number = int(number)
        number = ((1+number) * number) // 2
    list = []
    list.append(number)
    return jsonify(list[0])


@app.route('/sum.html', methods=['GET'])
def sum():
    return render_template('sum.html')


@app.route('/result',methods=['GET'])
def result():
    # number = request.args.get('number')  # 從HTML 抓 name= number 

    return jsonify(cities)


@app.route('/index2', methods=['GET','POST'])
def index2():
    return render_template('index.html')







####################################




if __name__ == "__main__":
    app.run(debug=True, port=2000)