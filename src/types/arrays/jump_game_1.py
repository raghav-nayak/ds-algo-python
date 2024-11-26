# https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150

# 55. Jump Game

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105

from typing import List

# my approach
def can_jump(nums: List[int]) -> bool:
    if not nums:
        return False

    nums_len = len(nums)

    if nums_len == 1 and nums[0] == 0:
        return True

    if nums_len > 1 and nums[0] == 0:
        return True

    if nums_len <= 2:
        return True

    index = 1
    while index < nums_len:
        value = nums[index]
        index += value

        if index == nums_len - 1:
            return True
        if index > nums_len - 1:
            return False
        if value == 0:
            return False

    return False

# private static boolean canJump(int[] nums) {
#     if (nums.length == 0 || nums.length == 1) {
#         return false;
#     }
#     int maxReachable = 0;
#     for (int idx = 0; idx < nums.length; idx++) {
#         maxReachable = Math.max(maxReachable, nums[idx] + idx);
#         if (nums[idx] == 0) {
#             if (idx + 1 == nums.length) {
#                 return true;
#             }
#             if (maxReachable == idx) {
#                 return false;
#             }
#         }
#     }
#     return true;
# }

# correct solution
def can_jump_kkn(nums: List[int]) -> bool:
    nums_len = len(nums)

    if nums_len == 0 or nums_len == 1:
        return True

    max_reachable = 0
    for index in range(nums_len):
        max_reachable = max(max_reachable, nums[index] + index)
        if nums[index] == 0:
            if index + 1 == nums_len:
                return True
            if max_reachable == index:
                return False
    return True

if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    print(can_jump(nums))
    print(can_jump_kkn(nums))

    nums = [3, 2, 1, 0, 4]
    print(can_jump(nums))
    print(can_jump_kkn(nums))

    nums = [1, 2]
    print(can_jump(nums))
    print(can_jump_kkn(nums))

    nums = [0, 1]
    print(can_jump(nums))
    print(can_jump_kkn(nums))

    nums = [2, 0, 0]
    print(can_jump(nums))
    print(can_jump_kkn(nums))
    
    nums = [0]
    print(can_jump(nums))
    print(can_jump_kkn(nums))
