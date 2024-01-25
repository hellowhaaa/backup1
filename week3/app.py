from flask import Flask, redirect, url_for, session, render_template, request, flash
import forms
import models
from forms import SumUpForm

DEBUG = True
LOCAL_HOST = ''

app = Flask(__name__)
app.secret_key = 'sdfjiohdgssdkghnlsdhildfs'


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
    return render_template('data.html', number=number)

# GTE POST pass the form to the template
@app.route('/save', methods=['POST'])
def save():
    return 'saved from route'
    # number = 0
    # form = SumUpForm()
    # # number = request.args.get('number')
    # if form.validate_on_submit():
    #     number = form.number.data  # 抓送出的資料回來
    #     flash('you did it!','success')
    #     # session['number'] = form.number.data
    #     redirect(url_for('result'))    
    # return render_template('sum.html', form=form, number = number)


# @app.route('/sum.html', methods =['GET', 'POST'])
# def sumup():
#     if request.method == 'POST':
#         return 'Hello' + request.values['number']
#     return render_template('sum.html')



@app.route('/result',methods=['POST'])
def result():
    number = request.args.get('number')  # 從HTML 抓 name= number 
    return render_template('result.html', number = number)




if __name__ == "__main__":
    app.run(debug=True, port=3000)