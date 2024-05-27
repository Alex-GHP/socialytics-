# Pseudocode:

    # if length of nums list == 0: return None

    # Initialize sum to 0

    # Iterate each num

    # Add each num to sum

    # return average -> sum / length of nums


def average(nums):
    if len(nums) == 0:
        return None
    sum = 0
    for num in nums:
        sum += num
    return sum / len(nums)

# O(n)

print(average([12, 12, 12]))