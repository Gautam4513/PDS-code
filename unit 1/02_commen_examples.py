# Full name as input
full_name = "John Doe"

# Find the index of the space between first and last name
space_index = full_name.index(" ")

# Slicing to extract first name and last name
# From start to space (index 0 to space_index-1)
first_name = full_name[:space_index]  
# From space (index space_index+1) to the end
last_name = full_name[space_index+1:] 

# Display the results
print("First Name:", first_name)
print("Last Name:", last_name)