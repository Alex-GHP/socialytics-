# Pseudocode

# Set minimum to infinity

# Iterate each num

# If current num is less than minimum, minimum takes it's value

# return minimum

def find_minimum(nums):
    minimum = float("inf")
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum

# O(n)

print(find_minimum([1, 3, 2, 69, 3, 5, 1]))