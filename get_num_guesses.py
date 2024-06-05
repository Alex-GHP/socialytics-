def get_num_guesses_recursive(length):
    if length == 0:
        return 0
    if length == 1:
        return 26
    return 26 ** length + get_num_guesses_recursive(length - 1)

# Time: O(n)
# Space: O(n)

def get_num_guesses(length):
    total = 0
    for i in range(length):
        total += 26 ** (i + 1)
    return total

# Time: O(n)
# Space: O(1)