# Assigment: Complete the num_possible_orders function. It takes as input the number of posts an influencer has in their schedule 
# and returns the total number of possible orders in which we could publish the posts.

def num_possible_orders(num_posts):
    if num_posts == 1:
        return 1
    return num_posts * (num_possible_orders(num_posts - 1))

print(num_possible_orders(5))