def swap_elements(lst, pos1, pos2):
    # Check if the positions are within the bounds of the list
    if pos1 < 0 or pos1 >= len(lst) or pos2 < 0 or pos2 >= len(lst):
        print("Invalid positions provided. Please enter valid indices.")
        return
    # Swap the elements
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    # Print the modified list
    print("List after swapping elements at positions", pos1, "and", pos2, ":", lst)

lst = [10, 20, 30, 40, 50]
pos1 = int(input("enter first position: "))
pos2 = int(input("enter second position: "))
swap_elements(lst, pos1, pos2)
