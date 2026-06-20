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
        lookup = {}
        cur = head
        while cur:
            copy = Node(cur.val)
            lookup[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = lookup[cur]
            copy.next = lookup[cur.next] if cur.next else None
            copy.random = lookup[cur.random] if cur.random else None
            cur = cur.next
        
        return lookup[head] if head else None