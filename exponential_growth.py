# Complete the exponential_growth function. Given the initial followers count n, growth factor factor, and number of days days, 
# return a list containing the exponential growth of followers for each day.

def exponential_growth(n, factor, days):
    list = [n]
    for i in range(days):
        list.append(list[len(list) - 1] * factor)
    return list

# O(factor^n)