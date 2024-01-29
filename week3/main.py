
def two_sum(nums, target):
    for i in range(len(nums)):
        other_number = target - nums[i]
        if other_number in nums:
            other_index = nums.index(other_number)
            return [i, other_index]


ans = two_sum([2, 7, 13, 18], 20)
print(ans)