from peewee import *

db = SqliteDatabase('students.db')
# 叫這個db students.db
"""
建立database
"""

"""
建立model 還有column name
"""
class Student(Model):
    username = CharField(max_length=255, unique=True)
    #  username needs to be unique attribute
    points = IntegerField(default=0)

    class Meta:
        database = db


students = [
    {'username': 'lily',
     'points': 48},
    {'username': 'ken',
        'points': 488},
    {'username': 'peter',
        'points': 4},
    {'username': 'prime',
        'points': 45},
]

"""
插入資料到database
"""
def add_students():
    for student in students:
        try:
            Student.create(username=student['username'],
                           points=student['points'])
        except IntegrityError:
            student_record = Student.get(username=student['username'])
            # get the student out of the database 讓他們的分數改變
            student_record.points = student['points']
            student_record.save()


# get top point student
def top_student():
    student = Student.select().order_by(Student.points.desc()).get()  # -> 大到小.get()得到first record
    # Student.select() -> 得所有資料
    return student  # 得 one row

if __name__ == "__main__":
    db.connect()  # -> connect to database
    db.create_tables([Student], safe=True)  # -> safe = True 表若database 或是table已經被建立了, 不會報錯
    # db.close()
    add_students()
    print('Our top student is : {0.username}'.format(top_student()))


