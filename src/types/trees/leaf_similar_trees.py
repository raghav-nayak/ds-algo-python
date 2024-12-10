# https://leetcode.com/problems/leaf-similar-trees/

# 872. Leaf-Similar Trees

# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.


# Example 1:
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true

# Example 2:
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false


# Constraints:
# The number of nodes in each tree will be in the range [1, 200].
# Both of the given trees will have values in the range [0, 200].

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_leaf_nodes(root: TreeNode, leaf_nodes: list):
    if root is None:
        return

    # leaf node condition check
    if not root.left and not root.right:
        leaf_nodes.append(root.val)
    else:
        get_leaf_nodes(root.left, leaf_nodes)
        get_leaf_nodes(root.right, leaf_nodes)


def leaf_similar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    root1_leaf_node = list()
    root2_leaf_node = list()
    get_leaf_nodes(root1, root1_leaf_node)
    get_leaf_nodes(root2, root2_leaf_node)

    if len(root1_leaf_node) != len(root2_leaf_node):
        return False

    for i in range(len(root1_leaf_node)):
        if root1_leaf_node[i] != root2_leaf_node[i]:
            return False

    return True
