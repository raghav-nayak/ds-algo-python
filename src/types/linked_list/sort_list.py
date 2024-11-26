# https://leetcode.com/problems/sort-list/description/?envType=study-plan-v2&envId=top-interview-150

# 148. Sort List

# Given the head of a linked list, return the list after sorting it in ascending order.
# Example 1:
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

# Example 2:
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]

# Example 3:
# Input: head = []
# Output: []

# Constraints:
# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105

# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_list(list_1, list_2):
    temp_node = ListNode(0)
    tail = ListNode(0)
    while list_1 and list_2:
        if list_1.val < list_2.val:
            tail.next, list_1 = list_1, list_1.next
        else:
            tail.next, list_2 = list_2, list_2.next
        tail = tail.next
    tail.next = list_1 or list_2
    return temp_node.next


def sort_list_chatgpt(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or head.next is None:
        return head

    slow_ptr, fast_ptr = head, head.next

    while fast_ptr and fast_ptr.next:
        slow_ptr, fast_ptr = slow_ptr.next, fast_ptr.next.next

    mid = slow_ptr.next
    slow_ptr.next = None

    left = sort_list_chatgpt(head)
    right = sort_list_chatgpt(mid)

    return merge_list(left, right)

def sort_ist_best_soln_leetcode(head: Optional[ListNode]) -> Optional[ListNode]:
    arr = list()
    temp = head
    while temp:
        arr.append(temp.val)
        temp = temp.next
    arr.sort()
    tmp = head
    for idx in arr:
        tmp.val = idx
        tmp = tmp.next
    return head


if __name__ == "__main__":
    head = [4, 2, 1, 3]
    print(sort_list_chatgpt(head))
