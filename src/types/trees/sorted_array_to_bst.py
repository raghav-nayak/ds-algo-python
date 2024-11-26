# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/?envType=study-plan-v2&envId=top-interview-150

# Given an integer array nums where the elements are sorted in ascending order, convert it to a
# height-balanced binary search tree.


# Example 1:
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.


# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in a strictly increasing order.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_array_to_BST(nums: List[int]) -> Optional[TreeNode]:
    if not nums:
        return None

    mid = len(nums) // 2

    root = TreeNode(nums[mid])
    root.left = sorted_array_to_BST(nums[:mid])
    root.right = sorted_array_to_BST(nums[mid + 1 :])

    return root


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    root = sorted_array_to_BST(nums)
    if root:
        print(root.val)

    nums = [1, 3]
    root = sorted_array_to_BST(nums)
    if root:
        print(root.val)
