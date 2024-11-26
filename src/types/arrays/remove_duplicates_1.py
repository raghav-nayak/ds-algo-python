# https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.


# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


# Constraints:

# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.


# approach : two pointers

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    nums_len = len(nums)

    if nums_len == 0:
        return 0

    index_1 = 0
    for index_2 in range(1, nums_len):
        if nums[index_1] != nums[index_2]:
            index_1 += 1
            nums[index_1] = nums[index_2]

    return index_1 + 1


def remove_duplicates_best_solution_from_leetcode(nums: List[int]) -> int:
    # Initialize the current position index.
    cur = 0
    # Initialize the variable to keep track of the last unique number processed.
    last = None
    # Iterate over each number in the input list.
    for n in nums:
        # If the current number is the same as the last unique number, skip it.
        if n == last:
            continue
        # Update the last unique number processed.
        last = n
        # Replace the element at the current position with the new unique number.
        nums[cur] = n
        # Move to the next position.
        cur += 1
    # Return the new length of the array after removing duplicates.
    return cur


if __name__ == "__main__":
    nums = [1, 1, 2]
    print(f"Number of unique numbers: {remove_duplicates(nums=nums)}")  # 2
    nums = [1, 1, 2]
    print(
        f"Number of unique numbers: {remove_duplicates_best_solution_from_leetcode(nums=nums)}"
    )  # 2

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(f"Number of unique numbers: {remove_duplicates(nums=nums)}")  # 5
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(
        f"Number of unique numbers: {remove_duplicates_best_solution_from_leetcode(nums=nums)}"
    )  # 5
