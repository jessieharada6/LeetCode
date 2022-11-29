# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        p0 = dummy = ListNode(next = head)
        
        for _ in range(left - 1):
            p0 = p0.next
        p1 = p0.next
        
        pre = None
        cur = p0.next
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        p0.next = pre
        p1.next = cur
        
        return dummy.next
class Solution:
    def __init__(self):
        self.s = None
            
    def reverseN(self, head, n): 
        if n == 1:
            self.s = head.next # n + 1
            return head

        last = self.reverseN(head.next, n - 1)
        head.next.next = head 
        head.next = self.s # connect to s
        return last
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == 1: 
            return self.reverseN(head, right) # provide the range
        
        btw = self.reverseBetween(head.next, left - 1, right - 1)
        head.next = btw
        return head 