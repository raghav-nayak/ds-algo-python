# Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/description/

# 209. Minimum Size Subarray Sum

# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0


# Constraints:
# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104


# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

from typing import List


def min_size_subarray_sum(nums: List[int], target: int) -> int:
    if not nums or target < 1:
        return -1

    min_elements = float("inf")
    start = 0
    sum = 0

    for end in range(len(nums)):
        sum += nums[end]
        while sum >= target:
            min_elements = min(min_elements, end - start + 1)
            sum -= nums[start]
            start += 1
    return min_elements if min_elements != float("inf") else 0


if __name__ == "__main__":
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    print(min_size_subarray_sum(nums, target))

    nums = [1, 4, 4]
    target = 4
    print(min_size_subarray_sum(nums, target))

    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    target = 11
    print(min_size_subarray_sum(nums, target))
    
