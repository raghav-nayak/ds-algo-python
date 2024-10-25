# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

# 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.


# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]


# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

from collections import deque
from typing import List


def search_range_brute_force(nums: List[int], target: int) -> List[int]:
    first = -1
    last = -1
    for idx, num in enumerate(nums):
        if num == target:
            if first == -1:
                first = idx
            last = idx

    return [first, last]


# partial: TODO: look into this
def search_range_recursive_impl(
    nums: List[int], target: int, start: int, end: int, result_list: deque
) -> List[int]:
    if start == end:
        return result_list
    mid = start + end // 2
    print(f"{start=} {end=} {mid=} {nums[mid]} {result_list=}")
    if nums[mid] == target:
        if not result_list:
            result_list.append(mid)
        else:
            if result_list[0] <= mid and mid <= result_list[1]:
                pass
            elif result_list[0] >= mid:
                result_list[0] = mid
            elif result_list[1] <= mid:
                result_list[1] = mid
            else:
                result_list.append(mid)
        search_range_recursive_impl(nums, target, start, mid - 1, result_list)
        search_range_recursive_impl(nums, target, mid + 1, end, result_list)
    elif nums[mid] < target:
        search_range_recursive_impl(
            nums=nums,
            target=target,
            start=mid + 1,
            end=end,
            result_list=result_list,
        )
    else:
        search_range_recursive_impl(
            nums=nums,
            target=target,
            start=start,
            end=mid - 1,
            result_list=result_list,
        )
    return result_list


def search_range_recursive(nums: List[int], target: int) -> List[int]:
    return list(
        search_range_recursive_impl(
            nums=nums,
            target=target,
            start=0,
            end=len(nums),
            result_list=deque(maxlen=2),
        )
    )


def find_element_index(nums: List[int], target: int, find_left: bool):
    left = 0
    right = len(nums) - 1
    index = -1
    while left <= right:
        mid_index = left + (right - left) // 2
        if nums[mid_index] == target:
            index = mid_index
            if find_left:
                right = mid_index - 1
            else:
                left = mid_index + 1
        elif nums[mid_index] < target:
            left = mid_index + 1
        else:
            right = mid_index - 1

    return index


def search_range_logN_kkn(nums: List[int], target: int):
    result = [-1, -1]
    result[0] = find_element_index(nums, target, True)
    result[1] = find_element_index(nums, target, False)
    return result


def search_range_logN_best_soln_leetcode(
    self, nums: List[int], target: int
) -> List[int]:
    l = 0
    r = len(nums) - 1

    l_lim = -1
    r_lim = -1
    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:

            r_lim = mid
            l = mid + 1

        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:

            l_lim = mid
            r = mid - 1

        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return [l_lim, r_lim]


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    # print(search_range_brute_force(nums, target))
    # print(search_range_recursive(nums, target))
    print(search_range_logN_kkn(nums, target))

    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    # print(search_range_brute_force(nums, target))
    print(search_range_logN_kkn(nums, target))

    nums = []
    target = 0
    # print(search_range_brute_force(nums, target))
    print(search_range_logN_kkn(nums, target))
