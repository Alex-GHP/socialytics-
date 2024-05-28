# Procedure bubble_sort(nums):
#     set swapping to True
#     set end to length of nums
#     while swapping is True:
#         set swapping to False
#         for i from 2nd element to end:
#             compare i - 1 element to i:
#               swap if necessary
#               set swapping to True
#         Reduce end by one
#     return nums
# End Proceduce

def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i-1] > nums[i]:
                temp = nums[i-1]
                nums[i-1] = nums[i]
                nums[i] = temp
                swapping = True
        end -= 1
    return nums

# O(n^2) | Best case: O(n)

print(bubble_sort([1, 3, 2, 5, 4]))
