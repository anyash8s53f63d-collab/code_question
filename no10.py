# Input Format

# The first line contains an integer n representing the number of existing product IDs.
# The second line contains n integers representing the product IDs in sorted order.
# The third line contains an integer newProductId, which represents the new product ID to be inserted.
# Constraints

# 1 ≤ n ≤ 1000
# The product IDs are integers and are sorted in non-decreasing order.
# The new product ID to be inserted is an integer.
# Output Format

# Output the new array with the product ID inserted at the correct position, maintaining the sorted order.

# Example 1

# Sample Input 1

# 5

# 101 105 110 120 130

# 107

# Sample Output 1

# 101 105 107 110 120 130

# Explanation

# The array is initially sorted as [101, 105, 110, 120, 130].

# The new product ID 107 is inserted in the correct position, between 105 and 110, resulting in the array [101, 105, 107, 110, 120, 130].

n = int(input())
arr = list(map(int, input().split()))
newProductId = int(input())

arr.append(newProductId)
arr.sort()

print(*arr)