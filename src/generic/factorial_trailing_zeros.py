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
    
    factorial_str = str()
    return count


if __name__ == "__main__":
    print(trailingZeroes(3))
    print(trailingZeroes(5))
    print(trailingZeroes(0))
    print(trailingZeroes(13))
    print(trailingZeroes(30))
