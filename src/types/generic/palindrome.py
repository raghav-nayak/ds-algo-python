# https://leetcode.com/problems/palindrome-number/submissions/1448814361/?envType=study-plan-v2&envId=top-interview-150

# 9. Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Constraints:
# -231 <= x <= 231 - 1


def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    
    original_number = x
    sum = 0
    while x > 0:
        rem = x % 10
        sum = sum*10 + rem
        x = x // 10
    return sum == original_number

def is_palindrome_best_soln_chatgpt(x: int) -> bool:
    if x < 0 :
        return False 
    xs = str(x)
    if len(xs)==1:
        return True
    ys = xs[::-1]
    return xs == ys

if __name__ == "__main__":
    x = 121
    print(is_palindrome(x))

    x = -121
    print(is_palindrome(x))

    x = 10
    print(is_palindrome(x))
