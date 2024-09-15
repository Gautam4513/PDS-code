def pattern_1(n):
    for i in range(1, n + 1):
        print('*' * i)

n = int(input("enter number n: "))
pattern_1(n)

def pattern_2(n):
    for i in range(n, 0, -1):
        print('$' * i)

n = int(input("enter number n: "))
pattern_2(n)

def pattern_3(n):

    # Upper part of the pattern
    for i in range(n, 0, -2):
        print('#' * i)
    
    # Lower part of the pattern (starting from 3, 5, etc.)
    for i in range(3, n + 1, 2):
        print('#' * i)

n = int(input("enter number n: ")) 
pattern_3(n)


