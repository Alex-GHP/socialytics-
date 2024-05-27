# Pseudocode

# Set sum equals 0 at the start

# Iterate each num

# Add each num to the total sum

# return sum

def sum(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

# O(n)

print(sum([1, 3, 2, 69, 3, 5, 1]))