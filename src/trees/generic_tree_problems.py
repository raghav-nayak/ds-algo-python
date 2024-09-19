from typing import List

from src.trees.binary_tree import BinaryTree, BNode, create_binary_tree

leaf_nodes_list = list()


def leaf_nodes(bnode: BNode) -> List[int]:

    if not bnode:
        return None

    curr_node = bnode
    if not (curr_node.left and curr_node.right):
        leaf_nodes_list.append(curr_node.data)
    leaf_nodes(curr_node.left)
    leaf_nodes(curr_node.right)
    return leaf_nodes_list


if __name__ == "__main__":
    binary_tree: BinaryTree = create_binary_tree(limit=7)
    print(leaf_nodes(bnode=binary_tree.get_root()))
