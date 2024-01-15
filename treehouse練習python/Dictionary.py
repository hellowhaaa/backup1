
# course = {'teacher': 'Ashley', 'title': 'Introducing Dictionaries', 'level': 'Beginner'}
#
# for item in course:
#      print(item)
# print(list(course.items()))
#
# for item in course.items():
#     print(item)
#
# for key, value in course.items():
#     print(key, value)
#
#
# def print_teacher(name, job, topic):
#     print(name)
#     print(job)
#     print(topic)
# print_teacher('Ashley', 'Instructor', 'Python')


#  利用kwargs 這個keyword argument(variable argument)
#  將變數包起來
def print_teacher(**kwargs):
    # 利用for loop 跑出 kwargs的內容
    for key, value in kwargs.items():
        print(f'{key}: {value}')


print_teacher(name='Ashley',  topic='Python', job='Instructor', second='java')
#   將 code 從positional argument 轉成 keyword
