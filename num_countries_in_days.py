# Write a function num_countries_in_days that takes a maximum amount of days max_days and the time increase factor factor, 
# then returns the number of countries an influencer can visit within that time limit. 
# Influencers start by spending one day in the first country and the growth factor is then applied to their visit to the next country.

def num_countries_in_days(max_days, factor):
    time_left = max_days
    count = 0
    time_in_country = 1

    while time_left >= time_in_country:
        time_left -= time_in_country
        count += 1
        time_in_country *= factor
    return count

# O(factor^n)