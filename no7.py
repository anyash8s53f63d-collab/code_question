# You are given the number of steps (or rows) of the staircase. Write a program to display the "right half pyramid" pattern, where each row contains a number of stars corresponding to the row number.

# Input Format
# The input consists of a single integer n that denotes the number of rows in the pyramid.

# Output Format
# The output should display the right half pyramid pattern using stars (*), where each row has a number of stars equal to the row number.

# Example 1
# Sample Input 1
# 5

# Sample Output 1

# *  
# * * 
# * * * 
# * * * * 
# * * * * *
# Explanation
# For n = 5, the pyramid has 5 rows.

# The first row has 1 star, the second row has 2 stars, and so on, until the fifth row, which has 5 stars.

# Example 2
# Sample Input 2
# 3

# Sample Output 2

# * 
# * *   
# * * *   
# Explanation
# For n = 3, the pyramid has 3 rows. The first row has 1 star, the second row has 2 stars, and the third row has 3 stars.

n = int(input())
for i in range(1, n + 1):
  print("* " * i)

