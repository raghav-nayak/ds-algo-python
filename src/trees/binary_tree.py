from collections import deque


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

    def get_size(self) -> int:
        return self.size


def create_binary_tree(limit: int) -> BinaryTree:
    binary_tree = BinaryTree()
    for data in range(limit):
        binary_tree.insert(data=data)
    return binary_tree


if __name__ == "__main__":
    binary_tree = create_binary_tree(limit=7)
