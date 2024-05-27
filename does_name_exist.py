# Assigment: Complete the does_name_exist function. It should loop over all of the first/last name combinations in the first_names and last_names lists. 
# If it finds a combination that matches the full_name it should return True. If the full name isn't found, it should return False instead.

# Pseudocode:

# Iterate every first name

# Iterate every last name

# If any combination of first name with the last name matches, return True

# return False

def does_name_exist(first_names, last_names, full_name):
    for first_name in first_names:
        for last_name in last_names:
            if f"{first_name} {last_name}" == full_name:
                return True
    return False

# O(n^2)

