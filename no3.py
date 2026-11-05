# Example 1
# Sample Input 1
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9

# Sample Output 1
# 1 2 3 6 5 4 7 8 9

# Explanation
# The matrix is:
# 1 2 3
# 4 5 6
# 7 8 9
# The zig-zag traversal order is:
# Row 0: left-to-right → 1 2 3
# Row 1: right-to-left → 6 5 4
# Row 2: left-to-right → 7 8 9
# Combining these, the output is: 1 2 3 6 5 4 7 8 9

# Example 2
# Sample Input 2
# 2 4
# 10 20 30 40
# 50 60 70 80

# Sample Output 2
# 10 20 30 40 80 70 60 50

# Explanation
# The matrix is:
# 10 20 30 40
# 50 60 70 80
# The zig-zag traversal order is:
# Row 0: left-to-right → 10 20 30 40
# Row 1: right-to-left → 80 70 60 50
# Combining these, the output is: 10 20 30 40 80 70 60 50

R, C = map(int, input().split())

matrix = []

for i in range(R):
    row = list(map(int, input().split()))
    matrix.append(row)

result = []

for i in range(R):
    if i % 2 == 0:
        result.extend(matrix[i])
    else:
        result.extend(matrix[i][::-1])

print(*result)