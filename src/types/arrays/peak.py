# # https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=top-interview-150


# 162. Find Peak Element

# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.


# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.


# Constraints:
# 1 <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
# nums[i] != nums[i + 1] for all valid i.


from typing import List


# initial approach
def find_peak_element(nums: List[int]) -> int:
    len_nums = len(nums)

    peak = 0
    if len_nums == 1:
        return peak

    if len_nums == 2:
        if nums[0] > nums[1]:
            peak = 0
        else:
            peak = 1
        return peak

    peak = 0
    for index in range(1, len_nums - 1):
        if nums[index - 1] < nums[index]:
            if nums[index] > nums[index + 1]:
                peak = index
                break
            else:
                peak = index + 1

    return peak

# this is wrong : we should not use Binary search here.
def find_peak_element_best_solution_leetcode(nums: List[int]) -> int:
    len_nums = len(nums)
    peak = 0
    if len_nums == 1:
        return peak

    if len_nums == 2:
        if nums[0] > nums[1]:
            peak = 0
        else:
            peak = 1
        return peak

    start = 1
    end = len_nums - 2

    while start <= end:
        mid = (start + end) // 2
        if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
            peak = mid
            break
        elif nums[mid] > nums[mid - 1]:
            start = mid + 1
        else:
            end = mid - 1
    return peak


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(f"{find_peak_element(nums=nums)}")
    print(f"{find_peak_element_best_solution_leetcode(nums=nums)}")

    nums = [1, 2, 1, 3, 5, 5, 4]
    print(f"{find_peak_element(nums=nums)}")
    print(f"{find_peak_element_best_solution_leetcode(nums=nums)}")
