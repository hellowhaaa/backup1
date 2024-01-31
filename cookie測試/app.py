from flask import (Flask, redirect, url_for, session, render_template, 
                   request, flash, make_response, jsonify)
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'sdfjiohdgssdkghnlsdhildfs'

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def index():
    return render_template("index.html", name=session.get('name'))


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        session['name'] = request.form.get("name")
        # session 其實是 empty dictionary with two columns ready to receive ky & value
        return redirect('/')
    return render_template("login.html")


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=8000)