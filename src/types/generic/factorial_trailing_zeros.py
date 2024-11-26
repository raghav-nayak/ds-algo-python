# https://leetcode.com/problems/factorial-trailing-zeroes/description/?envType=study-plan-v2&envId=top-interview-150

# 172. Factorial Trailing Zeroes
# Given an integer n, return the number of trailing zeroes in n!.

# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.


# Example 1:
# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.

# Example 2:
# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.

# Example 3:
# Input: n = 0
# Output: 0

# Constraints:
# 0 <= n <= 104

# Follow up: Could you write a solution that works in logarithmic time complexity?


memo = dict()


def factorial_n(n: int) -> int:
    if n <= 1:
        return 1
    if result := memo.get(n):
        return result

    memo[n] = n * factorial_n(n - 1)
    return memo[n]

# partial solution
def trailingZeroes(n: int) -> int:
    factorial = factorial_n(n)
    print(f"{factorial=}")
    count = 0
    # while factorial > 0:
    #     print(f"Inside while {factorial=}")
    #     rem = factorial % 10
    #     if rem != 0:
    #         break
    #     count += 1
    #     factorial = factorial / 10

    factorial_str = str(factorial)
    for idx in range(len(factorial_str) - 1, -1, -1):
        if factorial_str[idx] != "0":
            break
        count += 1

    return count


# ChatGPT approach
# The problem of counting the number of trailing zeroes in n! (the factorial of n) can be solved efficiently
# by considering the factors of 10 in n!. Each trailing zero in the factorial result is produced by a factor of
# 10, which is the product of 2 and 5.

# Key Insight:
# In any factorial, there are always more factors of 2 than factors of 5, so the number of trailing zeroes is
# determined by how many factors of 5 are present in the numbers from 1 to n.

# e.g. In the numbers from 1 to 5:
# - The multiples of 5 (e.g., 5, 10, 15, etc.) contribute a factor of 5 to the factorial.
# - Higher powers of 5 (like 25, 125, etc.) contribute additional factors of 5.

# Approach:
# To find the number of trailing zeroes in n!, we
# 1. Count how many multiples of 5 are in the numbers from 1 to n.
# 2. Count how many multiples of 25, 125, and so on are in the numbers from 1 to n, because they contribute
# additional factors of 5.


def trailingZeroes_chat_gpt(n: int) -> int:
    zeroes = 0
    while n >= 5:
        n //= 5
        zeroes += n
    return zeroes


if __name__ == "__main__":
    print(trailingZeroes(3)) # 0
    print(trailingZeroes(5)) # 1
    print(trailingZeroes(0)) # 0 
    print(trailingZeroes(13)) # 2
    print(trailingZeroes(30)) # 7
    # print(trailingZeroes(1574)) # failing - RecursionError: maximum recursion depth exceeded

    print(trailingZeroes_chat_gpt(1574))  # 390
