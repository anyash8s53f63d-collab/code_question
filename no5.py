# Example 1

# Sample Input 1

# 98631

# Sample Output 1

# 14

# Explanation

# Sum of odd digits: 9 + 3 + 1 = 13
# Sum of even digits: 8 + 6 = 14
# Since the sum of even digits is greater, the output is 14.
# Example 2

# Sample Input 2

# 274695

# Sample Output 2

# 21

# Explanation

# Sum of odd digits: 7 + 9 + 5 = 21
# Sum of even digits: 2 + 4 + 6 = 12
# Since the sum of odd digits is greater, the output is 21.

def OddEvenSum(num):
    odd_sum = 0
    even_sum = 0

    while num > 0:
        digit = num % 10

        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

        num //= 10

    return max(odd_sum, even_sum)


num = int(input())
print(OddEvenSum(num))