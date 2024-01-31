from peewee import *
import datetime
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash,check_password_hash


DATABASE = SqliteDatabase('social.db')


class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default=False)

    class Meta:
        database = DATABASE
        order_by = ('-join_at',)
        # 新的會在top

# 屬於某個class的方法，可以創建它所屬的class
# a method that belongs to a class that can create the class it belongs to
    @classmethod
    def create_user(cls, username,email, password, admin = False):
        try: cls.create(
            username = username,
            email = email,
            password = password,
            is_admin = admin)
        except IntegrityError:
            raise ValueError("User already exists")
        
def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe = True)
    DATABASE.close()
