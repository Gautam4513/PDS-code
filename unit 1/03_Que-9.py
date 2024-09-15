# Function to count vowels in a given string
def count_vowels(input_string):
    # Define the vowels (both lowercase and uppercase)
    vowels = "aeiouAEIOU"
    count = 0

    # Loop through each character in the string
    for char in input_string:
        if char in vowels:  # Check if the character is a vowel
            count += 1  # Increment the count if it's a vowel

    return count

# Input: User provides the string
user_string = input("Enter a string: ")

# Call the function to count vowels and print the result
vowel_count = count_vowels(user_string)
print(f"The number of vowels in the string is: {vowel_count}")