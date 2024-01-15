# def my_function(arg1, arg2, arg3, arg4):
#     print(arg)
#
# my_function(arg1="Hello", arg2="I", arg3="love", arg4="python")

#
# def my_function(*args):
#     for number in args:
#         print(str(number))
#
# my_function(1, 2, 3)



# def calculate_total(*args):
#     total = sum(args)
#     print(total)
#
# calculate_total(15,20,20,30)
#
# print(sum([15, 22]))
# print(sum((14, 22)))
# unpacker


# def unpacker():
#     return 'hey'
# def unpack():
#     return [4, 5, 6]
#
# var1, var2, var3 = unpacker()
# var4, var5, var6 = unpack()
# print(var1, var2, var3)
# print(var4, var5, var6)

first, last = input('Enter your fill name: \n').split()  # 回傳list
print(first)
print(last)

