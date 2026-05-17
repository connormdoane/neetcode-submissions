# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        pointer = head
        previous = None
        while pointer:
            tmp = pointer.next
            pointer.next = previous
            previous = pointer
            pointer = tmp
        return previous
