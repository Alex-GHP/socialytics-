# Pseudocode:

# For each index:
    # Set smallest_idx to the current index
    # For each index from smallest_idx+1 to the end of the list:
        # If the number at the inner index is smaller than the number at smallest_idx, set smallest_idx to the inner index
    # Swap the number at the current index with the number at smallest_idx

def selection_sort(nums):
    for i in range(len(nums)):
        small = i
        for j in range(small + 1, len(nums)):
            if nums[j] < nums[small]:
                small = j
        temp = nums[i]
        nums[i] = nums[small]
        nums[small] = temp
    return nums

# O(n^2)

print(selection_sort([1, 5, 2, 9, 4, 10, 2, 3]))
