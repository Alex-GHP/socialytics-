# Procedure:
    # Set low = 0
    # Set high = len(arr) - 1
    # while low <= high
        # set median to (low + high) // 2
        # if arr[median] == target 
            # return True
        # elif arr[median] < target 
            # low = median + 1
        # else 
            # high = median - 1
    # return False
# End

def binary_search(target, arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        median = (low + high) // 2
        if arr[median] == target:
            return True
        elif arr[median] < target:
            low = median + 1
        else:
            high = median - 1
    return False

# O(logn)

print(binary_search(3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))