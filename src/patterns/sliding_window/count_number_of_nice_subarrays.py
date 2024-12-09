# 1248. Count Number of Nice Subarrays

# https://leetcode.com/problems/count-number-of-nice-subarrays/description/

# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.


# Example 1:
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

# Example 2:
# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There are no odd numbers in the array.

# Example 3:
# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16


# Constraints:
# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.length

from collections import defaultdict
from typing import List


def number_of_subarrays(nums: List[int], k: int) -> int:
    first_odd_number_index = -1
    subarray_count = 0

    start = 0
    end = 0

    subarray_odd_num_count = 0
    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            if first_odd_number_index == -1:
                first_odd_number_index = i
                subarray_odd_num_count += 1
            elif subarray_odd_num_count != k:
                subarray_odd_num_count += 1
                end += 1
            else:
                end += 1
                subarray_count += 1
                for j in range(start, first_odd_number_index):
                    subarray_count += 1
    return subarray_count


def number_of_subarrays_kkn(nums: List[int], k: int) -> int:
    odd_num_count = 0
    subarray_count = 0
    frequency = defaultdict(int)

    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            odd_num_count += 1
        if odd_num_count - k in frequency:
            # if val := frequency.get(odd_num_count - k):
            subarray_count += frequency[odd_num_count - k]
        else:
            # frequency.update({odd_num_count - k: frequency[odd_num_count - k]})
            frequency[odd_num_count] = frequency[odd_num_count - k]
    return subarray_count




def number_of_subarrays_kkn_chatgpt_corrected(nums: List[int], k: int) -> int:
    odd_num_count = 0
    subarray_count = 0
    frequency = defaultdict(int)  # Use defaultdict to handle missing keys gracefully
    frequency[0] = 1  # Initialize for subarrays starting at the beginning

    for num in nums:
        if num % 2 != 0:
            odd_num_count += 1

        # Check if there is a valid subarray with `k` odd numbers
        if odd_num_count - k in frequency:
            subarray_count += frequency[odd_num_count - k]

        # Increment the count of subarrays with the current odd number count
        frequency[odd_num_count] += 1

    return subarray_count


def number_of_subarrays_best_soln_chatgpt(nums: List[int], k: int) -> int:
    odd_i = [-1] + [i for i, num in enumerate(nums) if num % 2] + [len(nums)]
    return sum(
        (odd_i[i] - odd_i[i - 1]) * (odd_i[i + k] - odd_i[i + k - 1])
        for i in range(1, len(odd_i) - k)
    )


if __name__ == "__main__":
    nums = [1, 1, 2, 1, 1]
    k = 3
    print(number_of_subarrays_best_soln_chatgpt(nums, k))

    nums = [2, 4, 6]
    k = 1
    print(number_of_subarrays_best_soln_chatgpt(nums, k))

    nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
    k = 2
    print(number_of_subarrays_best_soln_chatgpt(nums, k))
