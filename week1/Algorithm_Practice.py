def binary_search_position(numbers, target):
    low = 0
    high = len(numbers)
    while low < high:
        mid = (low + high) // 2
        if numbers[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


print(binary_search_position([1, 2, 5, 6, 7], 1))
print(binary_search_position([1, 2, 5, 6, 7], 6))