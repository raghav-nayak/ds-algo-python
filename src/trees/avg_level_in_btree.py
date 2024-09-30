# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150


# 637. Average of Levels in Binary Tree

# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.


# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].


# Example 2:
# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]


# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def average_of_levels(root: Optional[TreeNode]) -> List[float]:
    avg_sum = []
    if root is None:
        return avg_sum

    btree_queue = deque()
    btree_queue.append(root)

    while len(btree_queue) > 0:
        current_elements_count = len(btree_queue)
        sum = 0
        for _ in range(0, current_elements_count):
            elem = btree_queue.popleft()
            sum += elem.val
            if elem.left:
                btree_queue.append(elem.left)
            if elem.right:
                btree_queue.append(elem.right)
        avg_sum.append(float(sum / current_elements_count))
    return avg_sum


def average_of_levels_best_soln_leetcode(self, root: Optional[TreeNode]) -> List[float]:
    arr = []

    def helper(node, lvl):
        if not node:
            return
        if lvl == len(arr):
            arr.append([])

        arr[lvl].append(node.val)

        helper(node.left, lvl + 1)
        helper(node.right, lvl + 1)

    helper(root, 0)

    ret_arr = []
    for a in arr:
        ret_arr.append(sum(a) / len(a))

    return ret_arr


if __name__ == "__main__":
    root = [3, 9, 20, None, None, 15, 7]
    print(average_of_levels(root))
