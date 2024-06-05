import math

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        while n % i == 0:
            n /= i
            factors.append(i)
    if n > 2:
        factors.append(int(n))
    return factors

# Time: O(sqrt(2^s)) where s = log2(n) | exponential
# Space: O(logn)

print(prime_factors(49)) 