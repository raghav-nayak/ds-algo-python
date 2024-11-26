# https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150

# 189. Rotate Array

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]


# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105


# Follow up:

# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

from typing import List


def rotate_chatgpt_1(nums, k):
    n = len(nums)
    k = k % n  # To handle cases where k > n
    rotated = [0] * n
    for i in range(n):
        rotated[(i + k) % n] = nums[i]
    nums[:] = rotated  # Copy the rotated array back to nums


# Reverse the Array (In-place, O(1) space)
def rotate_chatgpt_2(nums, k):
    n = len(nums)
    k = k % n  # To handle cases where k > n

    # Helper function to reverse a portion of the array
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Reverse the whole array
    reverse(nums, 0, n - 1)
    # Reverse the first k elements
    reverse(nums, 0, k - 1)
    # Reverse the remaining n - k elements
    reverse(nums, k, n - 1)


def rotate_best_soln_leetcode(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]

    with open("user.out", "w") as Solution:
        for nums, k in zip(map(loads, stdin), map(int, stdin)):
            rotate(nums, k)
            Solution.write(f"{nums}\n".replace(" ", ""))
    exit()


if __name__ == "__main__":
    nums_1 = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate_chatgpt_1(nums_1, 6)
    print(nums_1)

    nums_2 = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate_chatgpt_1(nums_2, 6)
    print(nums_2)
