# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        p0 = dummy = ListNode(next = head)
        
        pre = None
        cur = head
        while n >= k:
            n -= k
            p1 = p0.next
            
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            
            nxt = p1
            p1.next = cur
            p0.next = pre
            p0 = nxt
        
        
        return dummy.next
        