# https://leetcode.com/problems/unique-binary-search-trees/description/?envType=problem-list-v2&envId=binary-tree

# 96. Unique Binary Search Trees
# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

# Example 1:
# Input: n = 3
# Output: 5

# Example 2:
# Input: n = 1
# Output: 1
 
# Constraints:
# 1 <= n <= 19

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def numTrees(self, n: int) -> List[Optional[TreeNode]]:
    pass
