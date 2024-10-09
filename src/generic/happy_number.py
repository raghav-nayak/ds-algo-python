# https://leetcode.com/problems/happy-number/?envType=study-plan-v2&envId=top-interview-150

# 202. Happy Number

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.


# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

# Example 2:
# Input: n = 2
# Output: false


# Constraints:
# 1 <= n <= 231 - 1


# def get_sum_square(num: int) -> int:
#     sum = 0
#     while num > 0:

#         rem = num % 10
#         sum += rem**2
#         num = num // 10
#     # print(f"1 {num=} {sum=}")
#     return sum


# def is_happy(n: int) -> bool:
#     sum = 0
#     num = n

#     while num != 1 and num != 0 and sum != num:
#         print(f"2 {num=} {sum=}")
#         sum = get_sum_square(num)
#         num = sum


#     if num == 1:
#         return True
#     else:
#         return False

def is_happy_chatgpt(n: int) -> bool:
    def sum_of_squares(num: int) -> int:
        return sum(int(digit) ** 2 for digit in str(num))

    seen_numbers = set()

    while n != 1:
        if n in seen_numbers:
            return False
        seen_numbers.add(n)
        n = sum_of_squares(n)

    return True

def getSquare(self, n):
    currentSum = 0
    while n != 0:
        remain = n % 10
        currentSum += remain * remain
        n = n // 10
    return currentSum

def isHappy(self, n: int) -> bool:
    slow = self.getSquare(n)
    fast = self.getSquare(self.getSquare(n))

    while (fast != slow) and (fast != 1):
        slow = self.getSquare(slow)
        fast = self.getSquare(self.getSquare(fast))

    return fast == 1


if __name__ == "__main__":
    print(is_happy_chatgpt(19))
    print(is_happy_chatgpt(2))
    print(is_happy_chatgpt(1111111))
