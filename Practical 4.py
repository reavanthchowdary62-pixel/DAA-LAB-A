# Practical-4: Factorial using Iterative and Recursive Function

import time

# Iterative Function
def factorial_iterative(n):
    factorial = 1

    for i in range(1, n + 1):
        factorial = factorial * i

    return factorial


# Recursive Function
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# User Input
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")

else:
    # Iterative Method
    start_time = time.perf_counter()
    result_iterative = factorial_iterative(n)
    end_time = time.perf_counter()

    iterative_time = end_time - start_time

    # Recursive Method
    start_time = time.perf_counter()
    result_recursive = factorial_recursive(n)
    end_time = time.perf_counter()

    recursive_time = end_time - start_time

    # Display Results
    print("\n----- Factorial Results -----")

    print("Number:", n)

    print("\nIterative Method:")
    print("Factorial:", result_iterative)
    print("Execution Time: {:.10f} seconds".format(iterative_time))
    print("Time Complexity: O(n)")
    print("Space Complexity: O(1)")

    print("\nRecursive Method:")
    print("Factorial:", result_recursive)
    print("Execution Time: {:.10f} seconds".format(recursive_time))
    print("Time Complexity: O(n)")
    print("Space Complexity: O(n)")


Enter a non-negative integer: 5

Number: 5

Iterative Method:
Factorial: 120
Execution Time: 0.0000012000 seconds
Time Complexity: O(n)
Space Complexity: O(1)

Recursive Method:
Factorial: 120
Execution Time: 0.0000015000 seconds
Time Complexity: O(n)
Space Complexity: O(n)
