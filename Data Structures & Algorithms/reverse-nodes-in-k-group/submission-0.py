# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupprev = dummy

        while True:
            kth = self.getKth(groupprev, k)
            if not kth:
                break
            groupnext = kth.next

            prev, cur = groupnext, groupprev.next
            while cur != groupnext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            temp = groupprev.next
            groupprev.next = kth
            groupprev = temp
        return dummy.next

    def getKth(self, cur, k):
        while cur and k:
            cur = cur.next
            k -= 1
        return cur