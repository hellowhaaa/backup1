import pymysql.cursors
from flask import Flask, render_template, request, redirect,url_for
from flask_bcrypt import generate_password_hash, check_password_hash
import re


db = pymysql.connect(host='localhost',
                     user='root',
                     password='password123',
                     database='assignment',
                     cursorclass=pymysql.cursors.DictCursor)
my_cursor = db.cursor()
print(my_cursor)

# delete_existing_table = "drop table if exists user"

# Create a database
# my_cursor.execute("CREATE DATABASE assignment")


#
#
# # Create table
# try:
#     # my_cursor.execute(delete_existing_table)
#     print("existing table has been deleted")
#     my_cursor.execute("CREATE TABLE user_test("
#                       "id int auto_increment primary key,"
#                       "email varchar(255),"
#                       "password varchar(255))")
#     print("user table has been created")
#
# except Exception as e:
#     print('exeception occured: ', e)
# my_cursor.close()

# Create a new record and iterate!!!!!!
# email = 'wang@gmail.com'
# password = 'password32111'
# query = "INSERT INTO `user` (`email`, `password`) VALUES ('wang@gmail.com', 'password32111')"
# query2 = "INSERT INTO `user` (`email`, `password`) VALUES (%s, %s)" % (email, password)
# my_cursor.execute(query)
# db.commit()


# Delete rows
# query3 = "DELETE FROM `user` WHERE email='wang@gmail.com'"
# my_cursor.execute(query3)
# db.commit()


# query2 = "SELECT `password` FROM `user` WHERE `email`=%s"
# my_cursor.execute(query2, ('wang@gmail.com',))
# # first_row = my_cursor.fetchone()  # 只會return first row, return tuple 或是 None
# # print(first_row)
# for row in my_cursor:
#     print(row['password'])


app = Flask(__name__)
app.secret_key = 'dfssdgfgd'
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def is_valid(email):
    if re.fullmatch(regex, email):
        return True
    else:
        return False


@app.route('/')
def index():
    wrong = request.args.get('wrong')
    return render_template('mysql.html', wrong=wrong)


@app.route('/member', methods=['GET', 'POST'])
def member():
    email = request.form.get('email')
    password = request.form.get('password')
    hashed_pw = generate_password_hash(password)
    if request.method == 'POST':
        if request.values['send'] == 'submit-sign-in':  # if button's value is submit-sign-in

            query1 = "SELECT `email` FROM `user_test` WHERE `email`=%s AND `password`=%s"
            my_cursor.execute(query1, (email, check_password_hash(hashed_pw, password)))
            if my_cursor.fetchone() is None:
                wrong = 'Your email or password is wrong'
                return redirect(url_for('index', wrong=wrong))
            else:
                return render_template('member.html', email=email)
        else:  # if button's value is submit-sign-up
            query3 = "SELECT `email` FROM `user_test` WHERE `email`=%s"
            my_cursor.execute(query3, email)
            if my_cursor.fetchone():
                wrong = 'The email address has been used!'
                return redirect(url_for('index', wrong=wrong))
            else:
                if is_valid(email):
                    query2 = "INSERT INTO `user_test`(`email`, `password`) VALUES (%s, %s)"
                    my_cursor.execute(query2, (email, check_password_hash(hashed_pw, password)))
                    db.commit()
                    return render_template('member.html', new_email=email)
                else:
                    wrong = 'The email address is invalid!'
                    return redirect(url_for('index', wrong=wrong))


if __name__ == '__main__':
    app.run(debug=True, port=4600)
