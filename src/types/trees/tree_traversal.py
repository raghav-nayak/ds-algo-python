# import os
# import sys
from collections import deque
from typing import List

from src.trees.binary_tree import BinaryTree, BNode, create_binary_tree

# sys.path.append(os.path.abspath(os.path.join("..", "ds-algo-python")))


class BinaryTreeTraversal:
    def __init__(self, btree: BinaryTree) -> None:
        self.btree: BinaryTree = btree

    def level_order_traversal(self) -> List[int]:
        result = list()

        if self.btree.get_size() == 0:
            return result

        result.append(self.btree.get_root())
        if self.btree.get_size() == 1:
            return result

        result = list()
        queue = deque()
        queue.append(self.btree.get_root())
        while len(queue) > 0:
            temp_bnode: BNode = queue.popleft()
            result.append(temp_bnode.data)
            if temp_bnode.left:
                queue.append(temp_bnode.left)
            if temp_bnode.right:
                queue.append(temp_bnode.right)
        return result

    def _pre_order(self, bnode: BNode, result: list):
        if bnode:
            result.append(bnode.data)
            self._pre_order(bnode=bnode.left, result=result)
            self._pre_order(bnode=bnode.right, result=result)

    def pre_order_traversal(self):
        result = list()
        self._pre_order(bnode=self.btree.get_root(), result=result)
        return result

    def _in_order(self, bnode: BNode, result: list):
        if bnode:
            self._in_order(bnode=bnode.left, result=result)
            result.append(bnode.data)
            self._in_order(bnode=bnode.right, result=result)

    def in_order_traversal(self):
        result = list()
        self._in_order(bnode=self.btree.get_root(), result=result)
        return result

    def _post_order(self, bnode: BNode, result: list):
        if bnode:
            self._post_order(bnode=bnode.left, result=result)
            self._post_order(bnode=bnode.right, result=result)
            result.append(bnode.data)

    def post_order_traversal(self):
        result = list()
        self._post_order(bnode=self.btree.get_root(), result=result)
        return result


if __name__ == "__main__":
    binary_tree_traversal = BinaryTreeTraversal(btree=create_binary_tree(limit=7))

    print(f"level order traversal : {binary_tree_traversal.level_order_traversal()}")
    print(f"pre-order traversal : {binary_tree_traversal.pre_order_traversal()}")
    print(f"in-order traversal : {binary_tree_traversal.in_order_traversal()}")
    print(f"in-order traversal : {binary_tree_traversal.post_order_traversal()}")
