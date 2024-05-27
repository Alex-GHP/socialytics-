# Socialytics needs a new tool that allows big brands to see how many of an influencer's followers are loyal to their brand. Complete the get_avg_brand_followers function. It takes two inputs:

# all_handles: a 2-dimensional list, or "list of lists" of strings representing instagram user handles on a per-influencer basis.
# brand_name: a string.
# get_avg_brand_followers returns the average number of handles that contain the brand_name across all the lists. Each list represents the audience of a single influencer.

# Pseudocode:

    # initialize loyal followers

    # Iterate in every list in the lists

    # Iterate in each list of that

    # if the brand_name is in the fan's name, increment loyal followers

    # return loyal followers

def get_avg_brand_followers(all_handles, brand_name):
    loyal = 0
    for lists in all_handles:
        for fan in lists:
            if brand_name in fan:
                loyal += 1
    return loyal / len(all_handles)

# O(nm)
