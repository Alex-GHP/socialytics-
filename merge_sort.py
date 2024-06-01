# merge_sort(nums) Procedure:
    # If the length of nums is less than 2
        # Return nums
    # Split the input array into two halves down the middle
    # Call merge_sort() twice, once on each half
    # Return the result of calling merge(l, r)
# End

# merge(first, second) Procedure:
    # Create a new "final" list of integers.
    # Set i and j equal to zero. They will be used to keep track of indexes in the input lists (A and B).
    # Use a loop to iterate over A and B at the same time. 
        # If an element in A is less than or equal to its respective element in B, add it to the final list and increment i. 
        # Else add the item in B to the final list and increment j.
    # After comparing all the items, there may be some items left over in either A or B (if one of the lists is longer than the other). Add those extra items to the final list.
    # Return the final list.
# End

def merge_sort(nums):
    if len(nums) < 2:
        return nums
    left = merge_sort(nums[:len(nums) // 2])
    right = merge_sort(nums[len(nums) // 2:])
    return merge(left, right)

def merge(left, right):
    final = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            j += 1
    while i < len(left):
        final.append(left[i])
        i += 1
    while j < len(right):
        final.append(right[j])
        j += 1
    return final

# O(nlog(n))

print(merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
