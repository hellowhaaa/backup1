def count(input):
    dic = {}
    for letter in input:
        if letter not in dic:
            times = 1
            dic[letter] = times
        else:
            dic[letter] += 1
    return dic


input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1))


def group_by_key(input):
    dic2 = {}
    for each in input:
        letter = each['key']
        digit = each['value']
        if letter in dic2:
            dic2[letter] += digit
        else:
            dic2[letter] = digit
    return dic2


input2 = [
    {'key': 'a', 'value': 3},
    {'key': 'b', 'value': 1},
    {'key': 'c', 'value': 2},
    {'key': 'a', 'value': 3},
    {'key': 'c', 'value': 5}
    ]
print(group_by_key(input2))