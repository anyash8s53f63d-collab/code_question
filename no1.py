# Example 1
# Sample Input 1
# Ram scored 91.62% in class 12 Board Exams.

# Sample Output 1
# 32

# Explanation
# Total alphabetic characters: 26
# Total numeric characters: 6
# Total alphanumeric characters: 26 + 6 = 32

# Example 2
# Sample Input 2
# Happy New Year 2016!!

# Sample Output 2
# 16

# Explanation
# Total alphabetic characters: 14
# Total numeric characters: 2
# Total alphanumeric characters: 14 + 2 = 16


s = input()

if len(s) == 0:
    print(-1)
else:
    count = 0
    for ch in s:
        if ch.isalnum():
            count += 1

    print(count)
