import pymysql.cursors
from flask import Flask, render_template, request

db = pymysql.connect(host='localhost',
                     user='root',
                     password='password123',
                     database='assignment',
                     cursorclass=pymysql.cursors.DictCursor)
my_cursor = db.cursor()

delete_existing_table = "drop table if exists user"

# Create a database
# my_cursor.execute("CREATE DATABASE assignment")

# create table
# try:
#     my_cursor.execute(delete_existing_table)
#     print("existing table has been deleted")
#     my_cursor.execute("CREATE TABLE user("
#                       "id int auto_increment primary key,"
#                       "email varchar(255),"
#                       "password varchar(255))")
#     print("user table has been created")
#
# except Exception as e:
#     print('exeception occured: ', e)
# my_cursor.close()

# Create a new record



app = Flask(__name__)
app.secret_key = 'dfssdgfgd'


@app.route('/')
def index():
    return render_template('mysql.html')


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    return render_template('signup.html')


@app.route('/member', methods=['GET', 'POST'])
def member():
    email = request.form.get('email')
    password = request.form.get('password')
    if request.method == 'POST':
        if email

        return render_template('member.html')



if __name__ == '__main__':
    app.run(debug=True, port=4600)
