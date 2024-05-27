# Pseudocode

# Set maximum to -infinity

# Iterate each num

# If current num is more than maximum, mmaximum takes it's value

# return maximum

def find_max(nums):
    max = float('-inf')
    for num in nums:
        if num > max:
            max = num
    return max

# O(n)

print(find_max([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))