from flask import (Flask, redirect, url_for, session, render_template, 
                   request, flash, make_response, jsonify)

import forms
import models

import json

DEBUG = True
LOCAL_HOST = ''

app = Flask(__name__)
app.secret_key = 'sdfjiohdgssdkghnlsdhidfs'



# tpe = {
#     "id": 0,
#     "city_name": "Taipei",
#     "country_name": "Taiwan",
#     "is_capital": True,
#     "location": {
#         "longitude": 121.569649,
#         "latitude": 25.036786
#     }
# }
# nyc = {
#     "id": 1,
#     "city_name": "New York",
#     "country_name": "United States",
#     "is_capital": False,
#     "location": {
#         "longitude": -74.004364,
#         "latitude": 40.710405
#     }
# }
# ldn = {
#     "id": 2,
#     "city_name": "London",
#     "country_name": "United Kingdom",
#     "is_capital": True,
#     "location": {
#         "longitude": -0.114089,
#         "latitude": 51.507497
#     }
# }
# cities = [tpe, nyc, ldn]

@app.route('/')
def index():
    word = 'Hello, My Server'

    return render_template('first_page.html', word=word)


@app.route('/data', methods=['GET','POST'])
def data():

    number = request.args.get('number')
    if number is None:
        number = 'Lack of Parameter'
    elif number.isalpha():
        number = 'Wrong Parameter'
    else:
        number = int(number)
        number = ((1+number) * number) // 2
    list = []
    list.append(number)
    return jsonify(list[0])


@app.route('/sum.html', methods=['GET', 'POST'])
def sum():
    if request.method == 'POST':
        number = request.form.get('number', type=int)
    return render_template('sum.html')















@app.route('/myname', methods=['GET', 'POST'])
def myname():
    data = get_saved_data()
    if request.method == "POST":
        return render_template("result.html", saves=data, input_name=data)
    else:
        return render_template("myname.html", saves=data)


# @app.route('/trackName', methods=['POST'])
# def trackName():
#     if request.method == 'POST':
#         input_name = request.args.get("input_name")
#
#         # HTTP, Set Cookie
#         response = make_response(redirect(url_for('result', input_name=input_name)))
#         data = get_saved_data()
#         data.update(dict(request.form.items()))
#         response.set_cookie('Name1', json.dumps(data))
#         # request.form -> immutable Multi Dict -> items() -> tuple key value pair
#         # 轉乘json string
#         return response


@app.route('/trackName', methods=['POST', 'GET'])
def trackName():
    if request.method == 'POST':
        input_name = request.args.get("input_name")

        # HTTP, Set Cookie
        response = make_response(redirect(url_for('result', input_name=input_name)))
        data = get_saved_data()
        data.update(dict(request.form.items()))
        response.set_cookie('Name1', json.dumps(data))
        # request.form -> immutable Multi Dict -> items() -> tuple key value pair
        # 轉乘json string
        return response



@app.route('/result', methods=['POST', 'GET'])
def result():
    input_name2, input_name = None, None
    if request.method == 'POST':
        input_name2 = request.form['name']
    else:
        input_name = request.args.get("input_name")
    return render_template('result.html', input_name=input_name, input_name2=input_name2)










def get_saved_data():
    try:
        data = json.loads(request.cookies.get('Name1')) #-> 又變回python dict
    except TypeError: #若不是cookie得到我們不能轉成jason的東西的話
        data = {}
    return data




####################################




if __name__ == "__main__":
    app.run(debug=True, port=9000)