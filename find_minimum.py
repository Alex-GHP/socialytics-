def find_minimum(nums):
    minimum = float("inf")
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum

print(find_minimum([1, 3, 2, 69, 3, 5, 1]))