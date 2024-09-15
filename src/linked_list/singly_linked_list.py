class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.count = 0

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
            temp_node = self.head
            while temp_node.next:
                temp_node = temp_node.next
            temp_node.next = node
        self.count += 1

    def print_nodes(self) -> None:
        temp_node = self.head
        print(f"Total nodes: {self.count}")
        while temp_node:
            print(f"{temp_node.data} -> ", end="")
            temp_node = temp_node.next
        print("null")


if __name__ == "__main__":
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.insert_at_beginning(10)
    singly_linked_list.insert_at_beginning(20)
    singly_linked_list.insert_at_end(30)
    singly_linked_list.insert_at_end(40)
    
    singly_linked_list.print_nodes()
