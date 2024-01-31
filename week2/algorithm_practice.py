def binary_search_first(numbers, target):
    low = 0
    high = len(numbers)
    while low < high:
        mid = (low + high) // 2
        if numbers[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 2))
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 5))
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 3))

