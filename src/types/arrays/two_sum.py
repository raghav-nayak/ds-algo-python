# https://leetcode.com/problems/two-sum/
#
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# examples:
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]


def two_sum(nums: list[int], target: int) -> list[int]:
    complement_map = dict()
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in complement_map:
            return [complement_map[complement], idx]
        complement_map[num] = idx

    return list()


if __name__ == "__main__":
    print(two_sum(nums=[2, 7, 11, 15], target=9))  # [0,1]
    print(two_sum(nums=[3, 2, 4], target=6))  # [1,2]
    print(two_sum(nums=[3, 3], target=6))  # [0,1]
    print(two_sum(nums=[9, 4, 3], target=2))  # []
