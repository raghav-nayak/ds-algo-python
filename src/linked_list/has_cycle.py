# https://leetcode.com/problems/linked-list-cycle/description/?envType=study-plan-v2&envId=top-interview-150

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.


# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).


# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.


# Constraints:
# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.

from src.linked_list.singly_linked_list import Node, SinglyLinkedList


def has_cycle(head: Node) -> bool:
    if not head or not head.next:
        return False

    slow_ptr = head
    fast_ptr = head.next

    while slow_ptr and fast_ptr and slow_ptr != fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr == fast_ptr


def has_cycle_best_solution_leetcode(head: Node) -> bool:
    if not head or not head.next:
        return False

    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True

    return False


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_end(3)
    sll.insert_at_end(2)
    sll.insert_at_end(0)
    sll.insert_at_end(-4)
    sll.create_cycle_with_end_node(source=-4, dest=2)
    print(has_cycle(sll.get_head()))

    sll_2 = SinglyLinkedList()
    sll_2.insert_at_end(3)
    sll_2.insert_at_end(2)
    sll_2.insert_at_end(0)
    sll_2.insert_at_end(-4)
    print(has_cycle(sll_2.get_head()))
