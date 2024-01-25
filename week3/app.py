from flask import Flask, redirect, url_for, session, render_template, request, flash, make_response

import forms
import models
from forms import SumUpForm
import json

DEBUG = True
LOCAL_HOST = ''

app = Flask(__name__)
app.secret_key = 'sdfjiohdgssdkghnlsdhildfs'


@app.route('/')
def index():
    word = 'Hello, My Server'
    data = get_saved_data()
    return render_template('first_page.html', word=word, saves = data)


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
    return render_template('data.html', number=number)

# GTE POST pass the form to the template
@app.route('/save', methods=['POST'])
def save():
    # import pdb; pdb.set_trace()
    response = make_response(redirect(url_for('result')))
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('character', json.dumps(data))
    # 給cookie 腳色名稱
    return response
    # number = 0
    # form = SumUpForm()
    # # number = request.args.get('number')
    # if form.validate_on_submit():
    #     number = form.number.data  # 抓送出的資料回來
    #     flash('you did it!','success')
    #     # session['number'] = form.number.data
    #     redirect(url_for('result'))    
    # return render_template('sum.html', form=form, number = number)



@app.route('/result')
def result():
    # number = request.args.get('number')  # 從HTML 抓 name= number 

    return render_template('result.html', saves = get_saved_data())







####################################



def get_saved_data():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError: #若不是cookie得到我們不能轉成jason的東西的話
        data = {}
    return data




if __name__ == "__main__":
    app.run(debug=True, port=3000)