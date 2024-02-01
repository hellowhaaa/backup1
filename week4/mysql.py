import pymysql.cursors
from flask import Flask, render_template, request, redirect,url_for

db = pymysql.connect(host='localhost',
                     user='root',
                     password='password123',
                     database='assignment',
                     cursorclass=pymysql.cursors.DictCursor)
my_cursor = db.cursor()

delete_existing_table = "drop table if exists user"

# Create a database
# my_cursor.execute("CREATE DATABASE assignment")




# Create table
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


@app.route('/')
def index():
    wrong = request.args.get('wrong')
    return render_template('mysql.html', wrong=wrong)


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    email = request.form.get('email')
    password = request.form.get('password')
    return render_template('signup.html')


@app.route('/member', methods=['GET', 'POST'])
def member():
    email = request.form.get('email')
    password = request.form.get('password')
    if request.method == 'POST':
        query2 = "SELECT `email` FROM `user` WHERE `email`=%s AND `password`=%s"
        my_cursor.execute(query2, (email, password))
        row = my_cursor.fetchone()
        if row is None:
            wrong = 'Your email or password is wrong'
            return redirect(url_for('index', wrong=wrong))
        else:
            ans = ''
            my_cursor.execute(query2, (email, password))
            for row2 in my_cursor:
                ans = row2['email']
                print(row2['email'])
            return render_template('member.html', ans=ans)





if __name__ == '__main__':
    app.run(debug=True, port=4600)
