# https://leetcode.com/problems/rotate-image/description/?envType=study-plan-v2&envId=top-interview-150

# 48. Rotate Image

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2:
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


# Constraints:
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000

from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    rotate_matrix = [[0] * rows for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            rotate_matrix[j][rows - i - 1] = matrix[i][j]

    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = rotate_matrix[i][j]

    return matrix

# not sure this is the right one
def rotate_best_soln_leetcode(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    l, r = 0, len(matrix[0]) - 1

    while l < r:
        for i in range(r - l):
            top = l
            bottom = r

            topLeft = matrix[top][l + i]

            matrix[top][l + i] = matrix[bottom - i][l]

            matrix[bottom - i][l] = matrix[bottom][r - i]

            matrix[bottom][r - i] = matrix[top + i][r]

            matrix[top + i][r] = topLeft
        r -= 1
        l += 1
    return matrix


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate(matrix))
    print(rotate_best_soln_leetcode(matrix))

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(rotate(matrix))
    print(rotate_best_soln_leetcode(matrix))
