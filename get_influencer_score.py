# get_influencer_score formula: average_engagement_percentage * log2(num_followers)

import math


def get_influencer_score(num_followers, average_engagement_percentage):
    return round(average_engagement_percentage * math.log(num_followers, 2))

# O(1)

print(get_influencer_score(750000, 0.7))