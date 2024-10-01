#!/usr/bin/env python3

def print_fibonacci(length):
    # Special case for length 0
    if length == 0:
        print([])  # Print an empty list for length 0
        return
    # Special case for length 1
    elif length == 1:
        print([0])  # Print [0] for length 1
        return
    
    # Initialize the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    
    # Generate the Fibonacci sequence until the desired length
    for i in range(2, length):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    
    # Print the entire sequence as a list
    print(fibonacci_sequence)
