# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

# 80. Remove Duplicates from Sorted Array II

# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

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

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


# Constraints:

# 1 <= nums.length <= 3 * 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

# approach : two pointers

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    same_as_last = False
    nums_len = len(nums)

    if nums_len == 0:
        return 0

    index_1 = 0
    for index_2 in range(1, nums_len):
        if same_as_last:
            if nums[index_1] == nums[index_2]:
                continue
            else:
                same_as_last = False
                index_1 += 1
                nums[index_1] = nums[index_2]

        else:
            if nums[index_1] == nums[index_2]:
                same_as_last = True

            index_1 += 1
            nums[index_1] = nums[index_2]

    return index_1 + 1

def remove_duplicates_best_solution_from_leetcode(nums: List[int]) -> int:
    j = 1
    for i in range(1, len(nums)):
        if j == 1 or nums[i] != nums[j-2]:
            nums[j] = nums[i]
            j += 1
    return j 

if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    print(f"Number of unique numbers: {remove_duplicates(nums=nums)}")  # 5
    # nums = [1, 1, 2]
    # print(
    #     f"Number of unique numbers: {remove_duplicates_best_solution_from_leetcode(nums=nums)}"
    # )  # 2

    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(f"Number of unique numbers: {remove_duplicates(nums=nums)}")  # 5
    # nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # print(
    #     f"Number of unique numbers: {remove_duplicates_best_solution_from_leetcode(nums=nums)}"
    # )  # 5
