# Procedure:
    # If n <= 1:
        # Return n
    # Hard core parent and grandparent
    # For each index in n - 1:
        # Set current value to equal parent + grandparent
        # Swap values for next iteration
    # Return current
# End

def fib(n):
    if n <= 1:
        return n
    current, parent, grandparent = 0, 1, 0
    for i in range(n - 1):
        current = parent + grandparent
        parent, grandparent = current, parent
    return current

# O(n)

print(fib(10))
