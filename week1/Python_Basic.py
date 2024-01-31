def find_max(numbers):
    if len(numbers) != 0:
        max_number = numbers[0]
        for number in numbers:
            if number > max_number:
                max_number = number
        return str(max_number)


def find_position(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return str(i)
    return '-1'


print(find_max([]))
print(find_max([5, 2, 7, 1, 6]))

print(find_position([5, 2, 7, 1, 6], 5))
print(find_position([5, 2, 7, 1, 6], 7))
print(find_position([5, 2, 7, 7, 7, 1, 6], 7))
print(find_position([5, 2, 7, 1, 6], 8))
