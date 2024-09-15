from datetime import datetime

def print_current_datetime():
    """
    Function to print the current date and time in a readable format.
    """
    current_datetime = datetime.now()
    print("Current date and time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))


print_current_datetime()
