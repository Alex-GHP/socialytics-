# Estimated spread for social meadia formula: estimated_spread = average_audience_followers * ( num_followers ^ 1.2 )

# Pseudocode:

    # Calculate the average of audience followers number

    # Get estimated spread using the formula above

def get_estimated_spread(audiences_followers):
    sum = 0
    for num in audiences_followers:
        sum += num
    average_audience_followers = sum / len(audiences_followers)

    return round(average_audience_followers * (len(audiences_followers) ** 1.2))

print(get_estimated_spread([10, 200, 3000, 5000, 4]))