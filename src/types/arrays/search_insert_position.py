# https://leetcode.com/problems/search-insert-position/description/?envType=study-plan-v2&envId=top-interview-150


# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4


# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

from typing import List


def search_insert(nums: List[int], target: int) -> int:
    start_pos = 0
    end_pos = len(nums)

    # while start_pos <= end_pos:
    #     mid = (start_pos + end_pos) // 2
    #     # print(f"{start_pos=} {end_pos=} {mid=}")
    #     if nums[mid] == target:
    #         return mid
    #     if nums[mid] >= target:
    #         end_pos = mid - 1
    #     else:
    #         start_pos = mid + 1

    # return start_pos

    while start_pos < end_pos:
        mid = (start_pos + end_pos) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            end_pos = mid - 1
        else:
            start_pos = mid + 1
    return start_pos


def search_insert_best_soln_leetcode(nums: List[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target or nums[i] > target:
            return i
    return len(nums)


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 5
    print(search_insert(nums, target))
    print(search_insert_best_soln_leetcode(nums, target))

    nums = [1, 3, 5, 6]
    target = 2
    print(search_insert(nums, target))
    print(search_insert_best_soln_leetcode(nums, target))

    nums = [1, 3, 5, 6]
    target = 7
    print(search_insert(nums, target))
    print(search_insert_best_soln_leetcode(nums, target))
