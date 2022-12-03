# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid
        p0 = p1 = head
        while p1 and p1.next:
            p1 = p1.next.next
            p0 = p0.next

        # reverse the second half
        cur = p0
        pre = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        
        # traverse to link nodes
        dummy = cur = head
        while cur.next and pre.next:
            cur_nxt = cur.next
            pre_nxt = pre.next
            
            cur.next = pre
            pre.next = cur_nxt
            
            cur = cur_nxt
            pre = pre_nxt

        cur = None