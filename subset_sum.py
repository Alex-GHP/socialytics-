def subset_sum(nums, target):
    memo = {}  # Dictionary for memoization
    return find_subset_sum(nums, target, len(nums) - 1, memo)

def find_subset_sum(nums, target, index, memo):
    if target == 0:
        return True
    if index < 0 and target != 0:
        return False
    if (target, index) in memo:  # Check if result is memoized
        return memo[(target, index)]

    if nums[index] > target:
        result = find_subset_sum(nums, target, index - 1, memo)
    else:
        result = find_subset_sum(nums, target, index - 1, memo) or \
                 find_subset_sum(nums, target - nums[index], index - 1, memo)

    memo[(target, index)] = result  # Store result for memoization
    return result

# Time: O(n * target)
# Space: O(n * target)