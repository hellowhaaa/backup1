import pymysql.cursors

db = pymysql.connect(host='localhost',
                     user='root',
                     password='password123',
                     database='assignment',
                     cursorclass=pymysql.cursors.DictCursor)

my_cursor = db.cursor()
print(my_cursor)


# insert_stmt = (
#     "INSERT INTO `user`(email, password)"
#     "VALUES (%s, %s)"
# )


insert_stmt = (
    "INSERT INTO `article` (title, content, author)"
    "VALUES (%s, %s, %s)"
)
for i in range(20, 23, 1):
    data = ('86-{}'.format(i), 'revenge', 20)
    try:
        # Executing the SQL command
        my_cursor.execute(insert_stmt, data)

        # Commit your changes in the database
        db.commit()
    except:
        # Rolling back in case of error
        db.rollback()

    print("Data inserted")

# Closing the connection
db.close()