
# Write a program that takes an array of positive integers representing the sizes of different animals and finds the maximum size using recursion.

# Input Format

# The first line contains an integer n (the number of animals). The second line contains n positive integers representing the sizes of the animals.

# Constraints

# 1≤n≤1000 Sizes are positive integers.

# Output Format

# Output the maximum size value from the array

# Example 1

# Sample Input 1

# 5

# 23 12 45 67 34

# Sample Output 1

# 67

# Explanation

# In the array [23, 12, 45, 67, 34], the maximum size is 67, which represents the largest animal.

# Example 2

# Sample Input 2

# 4

# 2 8 1 5

# Sample Output 2

# 8

# Explanation

# In the array [2, 8, 1, 5], the maximum size is 8, which represents the largest animal.

def find_max(arr, n):
    if n == 1:
        return arr[0]

    return max(arr[n - 1], find_max(arr, n - 1))


n = int(input())
arr = list(map(int, input().split()))

print(find_max(arr, n))