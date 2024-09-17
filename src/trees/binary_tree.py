from collections import deque
from typing import List


class BNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def insert(self, data: int) -> None:
        bnode = BNode(data)
        if not self.root:
            self.root = bnode
            return

        queue = deque()
        queue.append(self.root)

        while len(queue) > 0:
            temp_bnode: BNode = queue.popleft()
            if temp_bnode.left:
                queue.append(temp_bnode.left)
            else:
                temp_bnode.left = bnode
                self.size += 1
                return

            if temp_bnode.right:
                queue.append(temp_bnode.right)
            else:
                temp_bnode.right = bnode
                self.size += 1
                return

    def get_root(self) -> BNode:
        return self.root

    def level_order_traversal(self) -> List[int]:
        result = list()
        if self.size == 0:
            return result

        result.append(self.root)
        if self.size == 1:
            return result

        result = list()
        queue = deque()
        queue.append(self.root)
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
        self._pre_order(bnode=self.root, result=result)
        return result

    def _in_order(self, bnode: BNode, result: list):
        if bnode:
            self._in_order(bnode=bnode.left, result=result)
            result.append(bnode.data)
            self._in_order(bnode=bnode.right, result=result)

    def in_order_traversal(self):
        result = list()
        self._in_order(bnode=self.root, result=result)
        return result

    def _post_order(self, bnode: BNode, result: list):
        if bnode:
            self._post_order(bnode=bnode.left, result=result)
            self._post_order(bnode=bnode.right, result=result)
            result.append(bnode.data)

    def post_order_traversal(self):
        result = list()
        self._post_order(bnode=self.root, result=result)
        return result


if __name__ == "__main__":
    binary_tree = BinaryTree()
    binary_tree.insert(data="1")
    binary_tree.insert(data="2")
    binary_tree.insert(data="3")
    binary_tree.insert(data="4")
    binary_tree.insert(data="5")
    binary_tree.insert(data="6")
    binary_tree.insert(data="7")

    print(f"level order traversal : {binary_tree.level_order_traversal()}")
    print(f"pre-order traversal : {binary_tree.pre_order_traversal()}")
    print(f"in-order traversal : {binary_tree.in_order_traversal()}")
    print(f"in-order traversal : {binary_tree.post_order_traversal()}")
