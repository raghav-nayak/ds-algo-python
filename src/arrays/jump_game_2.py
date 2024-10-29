# https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150

# 45. Jump Game II
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [2,3,0,1,4]
# Output: 2

# Constraints:
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].

from time import sleep
from typing import List

# partial
def jump(nums: List[int]) -> int:
    i = 0
    step = 0
    while i < len(nums):
        j = nums[i]
        print(f"{i=} {nums[i]} {j=}")
        if i + j >= len(nums) - 1:
            step += 1
            return step

        k = 1
        max = -1
        index = -1
        while k <= j and k < len(nums):
            # print(f"{k=} {max=}")
            if nums[i + k] > max:
                max = nums[k]
                index = k
            k += 1
        print(f"{max=}")
        i = index
        step += 1
        sleep(1)
    return step


def jump_kkn(nums: List[int]) -> int:
    nums_len = len(nums)
    if nums_len <= 1:
        return 0

    curr_end = 0
    last_element = 0
    no_of_jumps_required = 0
    for idx in range(0, nums_len):
        last_element = max(last_element, nums[idx] + idx)
        if curr_end == idx:
            no_of_jumps_required += 1
            curr_end = last_element
            if curr_end >= nums_len - 1:
                break

    return no_of_jumps_required


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    # print(jump(nums)) # 2

    nums = [2, 3, 0, 1, 4]
    # print(jump(nums)) # 2

    nums = [3, 4, 3, 2, 5, 4, 3]
    # print(jump(nums)) # 3

    nums = [4, 1, 1, 3, 1, 1, 1]
    # print(jump(nums)) # 2

    nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]
    print(jump_kkn(nums))
