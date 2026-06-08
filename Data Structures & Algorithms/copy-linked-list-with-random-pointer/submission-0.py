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
        store = {None: None}
        cur = head

        while cur:
            copy = Node(cur.val)
            store[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = store[cur]
            copy.next = store[cur.next]
            copy.random = store[cur.random]
            cur = cur.next

        return store[head]