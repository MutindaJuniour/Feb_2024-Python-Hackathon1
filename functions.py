# Functions & Fibonacci Sequence
# Question
# Write a Python program to generate the Fibonacci sequence up to a specified term n. The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two preceding terms.
#We have provided  you with in-complete code, from the Knowledge learned from week 1 to week 3 please complete the missing parts to achieve the goal of the question.



# Your program should:

# Ask the user to input the value of n.
# Create a function that takes n as a parameter and returns a list containing the first n terms of the Fibonacci sequence.
# Print the generated Fibonacci sequence.

def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  # Initialize the first two terms of the sequence

    # Generating the Fibonacci sequence up to the nth term
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence[:n]  


def main():
    # prompt the for input an input value of n
    n = int(input("Enter the number of terms in the Fibonacci sequence: "))

    # Generate the Fibonacci sequence
    fibonacci_sequence = generate_fibonacci(n)

    # Print the generated Fibonacci sequence
    print("Fibonacci sequence up to term", n, ":", fibonacci_sequence)


if __name__ == "__main__":
    main()