# Constraints
# TC: O(n)
# ASC: O(1)

# Output Format
# The output contains a single integer representing the lucky number for the name decoded from the input.

# Explanation
# Find the alpha characters and find the sum of alphabetical values. The lucky number is the digital sum reduced up to a single digit.

s = input().strip()
total = 0

for ch in s:
    if ch.isalpha():
        total += ord(ch.upper()) - ord('A') + 1

while total >= 10:
    digit_sum = 0
    while total > 0:
        digit_sum += total % 10
        total //= 10
    total = digit_sum

print(total)