# geometric sequence formula: a_n = a_n * r^n-1

# Assigment:

# "fitness" influencers: follower count quadruples each month
# "cosmetic" influencers: follower count triples each month
# All other influencers: follower count doubles each month 

# Pseudocode:

    # Apply modified formula for each type of influencer

def get_follower_prediction(follower_count, influencer_type, num_months):
    if influencer_type == "fitness":
        return follower_count * (4 ** num_months)
    elif influencer_type == "cosmetic":
        return follower_count * (3 ** num_months)
    else:
        return follower_count * (2 ** num_months)
    
print(get_follower_prediction(10, "tech", 9))