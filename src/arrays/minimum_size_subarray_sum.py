# https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150

# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


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


# approach : sliding window

from collections import deque
from typing import List

# my approach
def min_subarray_len(target: int, nums: List[int]) -> int:
    if not nums or target < 1:
        return 0

    nums_len = len(nums)
    total_elements = deque()
    start = 0
    end = 0

    sum = 0
    min_elements = 9999

    while end < nums_len and start <= end:
        print(
            f"\n\nBefore: {start=} {end=} {nums[end]} {sum=} {min_elements=} {total_elements=}"
        )
        if sum < target:
            print(f"in < ")
            sum += nums[end]
            total_elements.append(nums[end])

        if sum == target:
            print(f"in == ")
            min_elements = min(min_elements, len(total_elements))
            total_elements.popleft()
            sum = sum - nums[start]
            start += 1
            sum = sum + nums[end]
            total_elements.append(nums[end])

        if sum > target:
            total_elements.popleft()
            sum = sum - nums[start]
            start += 1

        print(f"after: {start=} {end=} {min_elements=} {total_elements=}")

    if min_elements == 9999:
        min_elements = 0
    return min_elements


# chatgpt approach and best approach in leetcode
def min_subarray_len_chatgpt(target: int, nums: List[int]) -> int:
    if not nums or target < 1:
        return 0

    nums_len = len(nums)
    start = 0
    sum = 0
    # Set to infinity to handle cases when no subarray is found
    min_elements = float("inf")

    for end in range(nums_len):
        sum += nums[end]  # Add the current element to the sum

        # Shrink the window as long as the sum is greater than or equal to the target
        while sum >= target:
            # Update the minimum length if a smaller valid window is found
            min_elements = min(min_elements, end - start + 1)
            # Shrink the window from the left
            sum -= nums[start]
            start += 1

    # If no valid subarray was found, return 0
    return min_elements if min_elements != float("inf") else 0


if __name__ == "__main__":
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    # print(f"{min_subarray_len(target=target, nums=nums)}")

    target = 4
    nums = [1, 4, 4]
    # print(f"{min_subarray_len(target=target, nums=nums)}")

    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    # print(f"{min_subarray_len(target=target, nums=nums)}")

    target = 11
    nums = [1, 2, 3, 4, 5]
    print(f"{min_subarray_len(target=target, nums=nums)}")
