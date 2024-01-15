# groceries = ['roast beef', 'cucumbers', 'lettuce', 'peanut butter', 'bread', 'dog food']
#
# for index, item in enumerate(groceries, 1):
#     print(f'{index}. {item}')


# index = 1
# for item in groceries:
#     print(f'{index}. {item}')
#     index += 1

# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# nums_partial = nums[0::2]
# print(nums_partial)

# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# colors_partial = colors[::-1]
# print(colors_partial)

#
# docs = 'Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in). Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).'
# # if 'tuple' in docs:
# #     print("here")
# # else:
# #     print("not here")
#
# print(docs.count('tuple'))

# teacher = ['Lily', 'Lina', 'Owen', 'Lily']
# print(teacher.index('Lily'))

obj1 = [1, 2, 3, 4, 5]
obj2 = [6, 7, 8, 9, 10]

obj1 = obj1 + obj2
print(obj1)


a = 'abc'
d = 'def'
a = a+d
print(a)