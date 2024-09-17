class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.count = 0

    def get_head(self) -> Node:
        return self.head

    def insert_at_beginning(self, data) -> None:
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            node.next = self.head.next
            self.head.next = node
        self.count += 1

    def insert_at_end(self, data) -> None:
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = node
        self.count += 1

    def create_cycle_with_end_node(self, source: int, dest: int) -> None:
        dest_node = None
        curr_node = self.head
        while curr_node.next:
            if curr_node.data == dest:
                dest_node = curr_node
            curr_node = curr_node.next
        curr_node.next = dest_node

    def print_nodes(self) -> None:
        curr_node = self.head
        print(f"Total nodes: {self.count}")
        while curr_node:
            print(f"{curr_node.data} -> ", end="")
            curr_node = curr_node.next
        print("null")


if __name__ == "__main__":
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.insert_at_beginning(10)
    singly_linked_list.insert_at_beginning(20)
    singly_linked_list.insert_at_end(30)
    singly_linked_list.insert_at_end(40)

    singly_linked_list.print_nodes()
