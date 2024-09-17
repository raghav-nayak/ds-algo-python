#  https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150

# 169. Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109


from typing import List


def majority_element(nums: List[int]) -> int:
    nums_map = dict()

    for num in nums:
        val = nums_map.get(num)
        nums_map[num] = val + 1 if val else 1

    return max(nums_map, key=nums_map.get)


# could not understand this flow
def majority_element_best_solution_from_leetcode(nums: List[int]) -> int:
    curr_elem = nums[0]
    curr_len = 1
    idx = 1
    n = len(nums)
    while idx < n:
        ele = nums[idx]
        if ele == curr_elem:
            curr_len += 1
        elif curr_len > 1:
            curr_len -= 1
        elif curr_len == 1:
            curr_elem = nums[idx + 1]
            idx += 1
        idx += 1
    return curr_elem


if __name__ == "__main__":
    nums = [3, 2, 3]
    print(majority_element(nums))

    nums = [3, 2, 3]
    print(majority_element_best_solution_from_leetcode(nums))

    nums = [2, 2, 1, 1, 1, 2, 2]
    print(majority_element(nums))

    nums = [2, 2, 1, 1, 1, 2, 2]
    print(majority_element_best_solution_from_leetcode(nums))

    nums = [2, 2, 2, 1, 1, 1]
    print(majority_element_best_solution_from_leetcode(nums))

    nums = [2, 2, 2, 1, 1, 1]
    print(majority_element(nums))
