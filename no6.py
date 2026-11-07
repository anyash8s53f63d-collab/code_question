# Function Description:

# String replaceCharacter(String str, int n, char ch1, char ch2)

# The function accepts three arguments:
# str[]: A string str of length n containing only lowercase alphabets.
# n: The length of the string str[].
# ch1: The character to be replaced by ch2.
# ch2: The character to be replaced by ch1.
# The function modifies the string in place by swapping every occurrence of ch1 with ch2 and vice versa.
# Note

# If the string is empty, return null (None, in case of Python).
# If both characters ch1 and ch2 do not exist in the string or are the same, return the original string unchanged.
# Input Format

# A string str[] of lowercase alphabetical letters. Two characters ch1 and ch2.

# Output Format

# The modified string with ch1 and ch2 swapped wherever they occur.

# Example 1

# Sample Input 1

# apples

# a

# p

# Sample Output 1

# paales

# Explanation

# In the string "apples", every occurrence of 'a' is replaced with 'p', and every occurrence of 'p' is replaced with 'a', resulting in "paales".

# Example 2

# Sample Input 2

# bluecoloure

# l

# o

# Sample Output 2

# boueClolure

# Explanation

# In the string "bluecoloure", the character 'l' is replaced with 'o', and the character 'o' is replaced with 'l', resulting in "boueClolure".

def replaceCharacter(s, n, ch1, ch2):
    if not s:
        return None

    result = ""

    for ch in s:
        if ch == ch1:
            result += ch2
        elif ch == ch2:
            result += ch1
        else:
            result += ch

    return result


s = input().strip()
ch1 = input().strip()
ch2 = input().strip()

result = replaceCharacter(s, len(s), ch1, ch2)

if result is not None:
    print(result)
else:
    print("None")