# https://leetcode.com/problems/search-in-rotated-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

# 33. Search in Rotated Sorted Array

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1


# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104
from typing import List


def search(nums: List[int], target: int) -> int:
    if not nums:
        return -1

    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid

        # Check if the left half is sorted
        if nums[start] <= nums[mid]:
            # If the target is within the sorted left half
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1


if __name__ == "__main__":

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 5
    print(search(nums, target))

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(search(nums, target))

    nums = [5, 1, 3]
    target = 3
    print(search(nums, target))