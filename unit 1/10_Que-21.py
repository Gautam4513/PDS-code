def insert_string(string1, string2, position):

    if position < 0 or position > len(string1):
        return "Invalid position!"

    # Slicing the first string into two parts and inserting the second string in between
    result = string1[:position] + string2 + string1[position:]
    
    return result

# Input from the user (commented out to avoid automatic execution)
string1 = input("Enter the first string: ")
string2 = input("Enter the second string to insert: ")
position = int(input("Enter the position to insert the second string: "))

# Example usage:
# string1 = "Gujarat University"
# string2 = "Technological "
# position = 7

result = insert_string(string1, string2, position)
print("Result:", result)  
