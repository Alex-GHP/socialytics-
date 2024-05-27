# Complete the decayed_followers function.

# It calculates the final value of a quantity after a certain time has passed, given its initial value and a rate of decay. Return the remaining followers.

# remaining_total = quantity * ( retention_rate ^ time )

# The retention_rate is the opposite of fraction_lost_daily. If an influencer lost 0.2 (or 20%) of their followers each day, then the retention rate would be 0.8 (or 20%).

def decayed_followers(intl_followers, fraction_lost_daily, days):
    retention_rate = 1 - fraction_lost_daily
    return intl_followers * (retention_rate ** days)

# O(1)

print(decayed_followers(200, 0.5, 3))