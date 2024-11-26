# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150


# 153. Find Minimum in Rotated Sorted Array
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times.

# For example, the array nums = [0,1,2,4,5,6,7] might become:
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# Example 3:
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times.


# Constraints:
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.

from time import sleep
from typing import List


def find_min(nums: List[int]) -> int:
    nums_len = len(nums)
    if nums_len == 1:
        return nums[0]

    # if nums_len == 2:
    #     return nums[1] if nums[1] < nums[0] else nums[0]

    start = 0
    end = nums_len - 1
    while start < end:
        # mid = (start + end) // 2
        # print(f"start={nums[start]} mid={nums[mid]} end={nums[end]} ")
        # if nums[mid - 1] > nums[mid] and nums[mid] < nums[mid + 1]:
        #     print("1")
        #     return mid
        # elif nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
        #     print("2")
        #     start = nums[mid + 1] if nums[mid + 1] < nums[mid - 1] else nums[mid - 1]
        # elif nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
        #     print("2")
        #     end = mid - 1

        # print(f"{start=} {mid=} {end=}\n")

        mid = (start + end) // 2
        # print(f"start={nums[start]}, mid={nums[mid]}, end={nums[end]} ")

        if nums[mid] > nums[end]:
            start = mid + 1
        else:
            end = mid

    return nums[start]


if __name__ == "__main__":
    nums = [3, 4, 5, 1, 2]
    print(find_min(nums))

    nums = [4, 5, 6, 7, 0, 1, 2]
    print(find_min(nums))

    nums = [11, 13, 15, 17]
    print(find_min(nums))

    nums = [2, 1]
    print(find_min(nums))
