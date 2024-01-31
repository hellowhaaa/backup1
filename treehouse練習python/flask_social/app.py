from flask import Flask, g, render_template, flash, redirect, url_for
from flask_bcrypt import check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required
import models
import forms

DEBUG = True

app = Flask(__name__)
app.secret_key = 'dsfsdgds'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
# view之後會建立, 這一行在說 "若還沒login 則會 redirect 到一個叫做 login的頁面" 

# 建立一個function 給login manager 去look up the user
# user_loader -> 載入 user資料的函數
@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        # DoesNotExist from peewee
        return None

@app.before_request
def before_request(self):
    """
    connect to the database before each request
    """
    g.db = models.Database
    g.db.connect()


@app.after_request
def after_request(response):
    """
    close the database connect after each request
    """
    g.db.close()
    return response

@app.route('/register', methods=('GET', 'POST'))
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        flash("you did it!", 'success')
#         message category -> success
        models.User.create_user(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        return redirect(url_for('index'))
    return render_template('register.html', form = form)

# 在程式最上面有設置 名稱叫login
@app.route('/login', methods=('GET', 'POST'))
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.email == form.email.data)
        except models.DoesNotExist:
            flash('Your email or password doesn\'t match', "error")
            # category 給他 error
        else:
            if check_password_hash(user.password, form.password.data):
                login_user(user) # -> import 的工具
                flash("you logged in!", 'success')  # category -> success
                return redirect(url_for('index'))
            else:
                flash('Your email or password doesn\'t match', "error")
    return render_template('login.html', form =form)

@app.route('/logout')
@login_required  # 如果沒有log in 就會退出
def logout():
    logout_user()
    flash(' You have been logged out!')
    return redirect(url_for('index'))



if __name__ == "__main__":
    models.initialize()
    try:
        models.User.create_user(
            username = 'lily',
            email = 'fdsfg@gmail.com',
            password = 'password',
            admin = True
        )
    except ValueError:
        pass
    app.run(debug=DEBUG)