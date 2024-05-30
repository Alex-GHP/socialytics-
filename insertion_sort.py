# Pseudocode:
    # for each index in list

    # initialize j = i

    # while j > 0 and nums[j - 1] > nums[j]

    # swap nums[j - 1] with nums[j]

    # decrement j

    # return list

def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            temp = nums[j - 1] 
            nums[j - 1] = nums[j]
            nums[j] = temp
            j -= 1
    return nums

# O(n^2), best case: O(n)

print(insertion_sort([1, 3, 5, 2, 6, 7,  1, 10]))