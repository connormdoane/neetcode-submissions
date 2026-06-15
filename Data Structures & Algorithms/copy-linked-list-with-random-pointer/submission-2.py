"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None:None}

        p = head
        while p:
            copy = Node(p.val)
            oldToNew[p] = copy
            p = p.next
        p = head
        while p:
            copy = oldToNew[p]
            copy.next = oldToNew[p.next]
            copy.random = oldToNew[p.random]
            p = p.next
        
        return oldToNew[head]
            