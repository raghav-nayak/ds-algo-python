# https://leetcode.com/problems/validate-binary-search-tree/description/?envType=problem-list-v2&envId=binary-tree

# 98. Validate Binary Search Tree

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Example 1:
# Input: root = [2,1,3]
# Output: true

# Example 2:
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


# my approach partial
def isValidBST(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    if root.left and root.right:
        if root.left.val < root.val and root.right.val > root.val:
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        else:
            return False
    elif root.left and root.left.val < root.val:
        return self.isValidBST(root.left)
    elif root.right and root.right.val > root.val:
        return self.isValidBST(root.right)
    # if root.left and root.left.val < root.val:
    #     left = self.isValidBST(root.left)
    # if root.right and root.right.val > root.val:
    #     right = self.isValidBST(root.right)

    return False


def isValidBST_chatgpt(root: Optional[TreeNode]) -> bool:
    if not root:
        return True  # An empty tree is a valid BST

    # Helper function to validate the tree with min and max constraints
    def validate(node, low, high):
        if not node:
            return True  # Base case: An empty node is valid

        # Check if the current node's value is within the allowed range
        if not (low < node.val < high):
            return False

        # Recursively validate the left and right subtrees
        return validate(node.left, low, node.val) and validate(
            node.right, node.val, high
        )

    # Call the helper function with the full range of values
    return validate(root, float("-inf"), float("inf"))

def isValidBST_best_soln_leetcode(self, root: Optional[TreeNode]) -> bool:
    
    def validate(node, low=None, high=None):
        if not node:
            return True

        if low != None and node.val <= low:
            return False
        
        if high != None and node.val >= high:
            return False
        
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)
    
    return validate(root)