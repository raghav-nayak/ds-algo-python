# https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=top-interview-150


# 199. Binary Tree Right Side View

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.


# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# Example 2:
# Input: root = [1,null,3]
# Output: [1,3]

# Example 3:
# Input: root = []
# Output: []


# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution using DFS : partial
def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    output = list()
    return self.rightSideViewImpl(root, output)


def rightSideViewImpl(self, root: Optional[TreeNode], output: List[TreeNode]):
    if not root:
        return root

    output.append(root.val)
    if root.right:
        self.rightSideViewImpl(root=root.right, output=output)
    return output


def rightSideView_chatgpt(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    # Initialize a deque for level-order traversal
    queue = deque([root])
    right_side = []

    while queue:
        level_length = len(queue)

        # Traverse the current level
        for i in range(level_length):
            node = queue.popleft()

            # Capture the last node of each level (rightmost node)
            if i == level_length - 1:
                right_side.append(node.val)

            # Add the child nodes in the queue (left first, then right)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return right_side


def rightSideView_best_soln_leetcode(self, root: Optional[TreeNode]) -> List[int]:
    def bfs(root):
        q = deque()
        if root:
            q.append(root)
        res = []
        rightSide = None

        while len(q) > 0:
            for _ in range(len(q)):
                curr = q.popleft()
                rightSide = curr

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            if rightSide:
                res.append(rightSide.val)
        return res

    return bfs(root)
