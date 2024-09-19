# https://leetcode.com/problems/kth-largest-element-in-an-array/?envType=study-plan-v2&envId=top-interview-150

# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?


# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4


# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104


import heapq

from src.heap.custom_heap_implementation import MaxHeap


def kth_largest(nums: list, k: int):
    max_heap = MaxHeap()
    for num in nums:
        max_heap.insert(num)

    kth_largest = None
    for i in range(k):
        kth_largest = max_heap.extract_max()

    return kth_largest


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    # print(heapq.nlargest(k, nums)[-1])
    print(kth_largest(nums, k))

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    # print(heapq.nlargest(k, nums)[-1])
    print(kth_largest(nums, k))
