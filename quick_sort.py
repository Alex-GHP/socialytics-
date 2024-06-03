# quick_sort(nums, low, high) Procedure:
    # If low is less than high:
        # Partition the input list
        # quick_sort(left side)
        # quick_sort(right side)
# End

# partition(nums, low, high) Procedure:
    # Set pivot to num of index high
    # Set i to low
    # For each index from low to high:
        # If nums[j] is less than pivot:
            # Swap nums[i] with nums[j]
            # Increment i
    # Swap nums[i] with nums[high]
    # Return i
# End

# quick_sort_shuffle(nums) Procedure:
    # randomly shuffle the list beofre to ensure O(nlog(n))
    # quick_sort() the list
# End

import random

def quick_sort(nums, low, high):
    if low < high:
        p = partition(nums, low, high)
        quick_sort(nums, low, p - 1)
        quick_sort(nums, p + 1, high)

def partition(nums, low, high):
    p = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < p:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i

def quick_sort_shuffle(nums):
    random.shuffle(nums)
    quick_sort(nums, 0, len(nums) - 1)

# O(nlog(n))

nums = [3, 6, 8, 10, 1, 2, 1]
quick_sort_shuffle(nums)
print(nums)  