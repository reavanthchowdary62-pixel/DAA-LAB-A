# Practical 1: Sorting Algorithms

This practical implements Selection Sort, Bubble Sort, and Merge Sort, insertion sort, quick sort 
Each algorithm includes implementation, time complexity analysis (best, worst, and average cases), and execution time measurement.

# Practical 2: 

This practical implements the Linear Search algorithm with interactive user input.
It demonstrates:
- Implementation of linear search that returns the index of the target (or -1 if not found).
- Measurement of execution time using `time.perf_counter()`.
- Time complexity analysis (Best, Average, Worst cases).

Usage:
- Interactive: run the script and follow prompts to provide the list and target value.
- Demo: run the script with a demo flag (if provided in the script).
1. linear search 
2. binary search

# Practical 3:Min-Heap and Max-Heap Sort
Description:

This project implements Heap Sort in Python using heapq.

Min-Heap: Sorts elements in ascending order.
Max-Heap: Sorts elements in descending order.
Features
Takes user input for array elements.
Uses heapq.heapify() and heapq.heappop().
Measures execution time using time.perf_counter().
Displays time complexity.
Example

Min-Heap:

Input: 25, 14, 36, 85, 96
Output: [14, 25, 36, 85, 96]

Max-Heap:

Input: 25, 78, 89, 45, 56, 33
Output: [89, 78, 56, 45, 33, 25]
Complexity
Best Case: O(n log n)
Average Case: O(n log n)
Worst Case: O(n log n)
Space Complexity: O(n)
Requirements
Python 3
heapq and time modules (built-in)
Conclusion

The program demonstrates how Min-Heap and Max-Heap can be used to efficiently sort an array in ascending and descending order

 # Practical 4:
 ## Factorial Using Iterative and Recursive Function
Description

This Python program calculates the factorial of a non-negative integer using two methods:

### Iterative method
### Recursive method

It also compares the execution time and complexity of both methods.

Example

Input:

Enter a non-negative integer: 5


Output:

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

Complexity
Method	Time	Space
Iterative	O(n)	O(1)
Recursive	O(n)	O(n)
Requirements
Python 3.x
Run
python factorial.py

Conclusion

Both methods produce the same factorial result. The iterative method uses less memory, while the recursive method demonstrates the use of recursion.

# PRACTICAL 7
# Coin Change Problem Using Dynamic Programming

This project provides a Python solution to the Coin Change Problem using Dynamic Programming. The program determines the minimum number of coins required to make a given target amount from a set of available coin denominations.

The algorithm builds a dynamic programming table to store the minimum coins needed for every amount from `0` to the target value. By reusing previously computed results, it efficiently finds the optimal solution and avoids redundant calculations.

If the target amount can be formed, the program returns the minimum number of coins required. Otherwise, it returns `-1` to indicate that no valid combination exists.

### Features

* Efficient Dynamic Programming approach
* Finds the minimum number of coins required
* Handles impossible cases by returning `-1`
* Simple and easy-to-understand Python implementation

### Complexity

* **Time Complexity:** O(n × amount)
* **Space Complexity:** O(amount)

This project is useful for learning Dynamic Programming concepts, practicing algorithm design, and preparing for coding interviews.
# Practical 5 

## Aim

# To implement the **0/1 Knapsack Problem** using the **Dynamic Programming** technique and find the maximum value that can be obtained without exceeding the given knapsack capacity.

---

## Problem Statement

The **0/1 Knapsack Problem** is an optimization problem where a set of items is given, and each item has:

- A weight
- A value

The objective is to select items such that the **total value is maximum**, while the **total weight does not exceed the capacity of the knapsack**.

Each item can be selected **only once**.

---

## Algorithm Used

### Dynamic Programming

A 2D DP table is used to solve the problem.

`dp[i][w]` represents the maximum value that can be obtained using the first `i` items with a knapsack capacity of `w`.

For every item, two choices are considered:

1. **Include the item**
2. **Exclude the item**

The maximum value from these two choices is stored in the DP table.

---

## Input

The program takes the following inputs from the user:

- Number of items
- Weight of each item
- Value of each item
- Maximum capacity of the knapsack

---

## Output

The program displays:

- Maximum value
- Selected items
- Execution time
- Time complexity
- Space complexity
