# Pseudocode:

    # if length of nums list == 0: return None

    # Sort the list of numbers

    # If length of list is even: return the average of the 2 median numbers

    # Else return the median number


def median(nums):
    if len(nums) == 0:
        return None
    nums = sorted(nums)
    n = len(nums)
    if n % 2 == 0:
        return (nums[n // 2] + nums[n // 2 - 1]) / 2
    return nums[n // 2]

# O(1)

print(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))