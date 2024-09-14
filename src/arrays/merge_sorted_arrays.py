# https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# examples

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    last_index = m + n - 1
    num1_index = m - 1
    num2_index = n - 1

    while num1_index >= 0 and num2_index >= 0:
        if nums1[num1_index] > nums2[num2_index]:
            nums1[last_index] = nums1[num1_index]
            num1_index -= 1
        else:
            nums1[last_index] = nums2[num2_index]
            num2_index -= 1

        last_index -= 1

    while num2_index >= 0:
        nums1[last_index] = nums2[num2_index]
        num2_index -= 1
        last_index -= 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1=nums1, m=m, nums2=nums2, n=n)
    print(f"{nums1=}")

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    merge(nums1=nums1, m=m, nums2=nums2, n=n)
    print(f"{nums1=}")
    
    nums1 = [0]
    m = 0
    nums2 = [0]
    n = 0
    merge(nums1=nums1, m=m, nums2=nums2, n=n)
    print(f"{nums1=}")
    

