def fibonacci_sequence(n):
    """
    Function to generate and print Fibonacci sequence up to the nth term.
    """
    if n <= 0:
        print("Please enter a positive integer.")
        return
    elif n == 1:
        print("Fibonacci sequence up to 1 term: 0")
        return
    elif n == 2:
        print("Fibonacci sequence up to 2 terms: 0, 1")
        return

    # Start with first two Fibonacci numbers
    fib_sequence = [0, 1]

    # Generate the Fibonacci sequence
    for i in range(2, n):
        next_number = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_number)

    # Print the Fibonacci sequence
    print(f"Fibonacci sequence up to {n} terms: {', '.join(map(str, fib_sequence))}")

n = int(input("enter the number: "))
fibonacci_sequence(n)
