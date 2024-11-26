# Problem: Given an array of integers and a number k, find the maximum sum of any contiguous subarray of size k.

# Example:
# Input: arr = [1, 2, 3, 4, 5], k = 2
# Output: 9 (Subarray [4, 5] has the maximum sum.)

from typing import List


def max_sum_subarray_size_k(arr: List[int], k: int) -> int:
    if len(arr) < k:
        return -1

    max_sum = 0
    for i in range(0, k):
        max_sum += arr[i]

    sum = max_sum
    for j in range(k, len(arr)):
        sum += arr[j] - arr[j - k]
        if sum > max_sum:
            max_sum = sum
    return max_sum


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 2
    print(max_sum_subarray_size_k(arr, k))

    arr = [
        100,
        400,
        200,
        300,
    ]
    k = 2
    print(max_sum_subarray_size_k(arr, k))
