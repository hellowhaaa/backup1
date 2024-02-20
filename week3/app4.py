from flask import (Flask, redirect, url_for, session, render_template, 
                   request, flash, make_response, jsonify)

import forms
import models

import json

DEBUG = True
LOCAL_HOST = ''

app = Flask(__name__)
app.secret_key = 'sdfjiohdgssdkghnlsdhidfs'




@app.route('/')
def index():
    word = 'Hello, My Server'

    return render_template('first_page.html', word=word)


@app.route('/data', methods=['GET', 'POST'])
def data():
    number = request.args.get('number')
    if number is None:
        number = 'Lack of Parameter'
    elif number.isalpha():
        number = 'Wrong Parameter'
    else:
        number = int(number)
        number = ((1+number) * number) // 2
    return jsonify(number)


@app.route('/sum.html', methods=['GET', 'POST'])
def sum():
    if request.method == 'POST':
        number = request.form.get('number', type=int)
    return render_template('sum.html')


@app.route('/myname', methods=['GET', 'POST'])
def myname():
    if request.method == "POST":
        name = request.cookies.get('name')
        return render_template("myname.html", name=name)
    else:
        return render_template("myname.html")


@app.route('/trackName', methods=['POST', 'GET'])
def trackName():
    if request.method == 'POST':
        user = request.form['name']
        response = make_response(render_template('myname.html'))
        response.set_cookie('name', user)
        return response
    else:
        name = request.args.get("name")
        return render_template('myname.html', name=name)


if __name__ == "__main__":
    app.run(debug=True, port=9000)