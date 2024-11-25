# https://leetcode.com/problems/triangle/description/?envType=study-plan-v2&envId=top-interview-150

# 120. Triangle

# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.


# Example 1:

# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
# Example 2:

# Input: triangle = [[-10]]
# Output: -10


# Constraints:

# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -104 <= triangle[i][j] <= 104


# Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?

from typing import List

# def minimum_total(triangle: List[List[int]]) -> int:
#     min_total = 0
#     # last_position = 0
#     for i in range(0, len(triangle)):
#         row = triangle[i]
#         print(f"\n{row=}")
#         min_total += row[0]
#         print(f"{min_total=}")
#     return min_total


def min_total_chat_gpt(triangle: List[List[int]]) -> int:
    # Start from the last row and move upward
    n = len(triangle)
    dp = triangle[-1]  # Initialize DP with the last row

    # Process rows from second last to the top
    for i in range(n - 2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = triangle[i][j] + min(
                dp[j], dp[j + 1]
            )  # Update DP for the current row

    return dp[0]  # The top of the triangle contains the minimum path sum


def minimum_total_best_soln_leetcode(triangle: List[List[int]]) -> int:
    # Start from the second-last row and accumulate the minimum path sum to the top
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # Update each element to be the minimum path sum at that position
            triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

    # The top element now contains the minimum path sum
    return triangle[0][0]


if __name__ == "__main__":
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(min_total_chat_gpt(triangle))

    triangle = [[-10]]
    print(min_total_chat_gpt(triangle))

    triangle = [[-1], [2, 3], [1, -1, -3]]
    print(min_total_chat_gpt(triangle))
