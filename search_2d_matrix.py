def search_2d_matrix(lists, target):
    for list in lists:
        low = 0
        high = len(list) - 1
        while low <= high:
            median = (low + high) // 2
            if list[median] == target:
                return True
            elif list[median] < target:
                low = median + 1
            else:
                high = median - 1
    return False

print(search_2d_matrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 69))