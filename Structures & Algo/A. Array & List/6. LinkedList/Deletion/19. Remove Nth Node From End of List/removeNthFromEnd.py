class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# kind of one pass
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = p1 = p2 = ListNode(next = head)
        
        for _ in range(n):
            p1 = p1.next
    
        while p1.next:
            p1 = p1.next
            p2 = p2.next

        
        p2.next = p2.next.next
        return dummy.next


# get length, then iterate
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        m = 0
        cur = head
        while cur:
            m += 1
            cur = cur.next
        
        dummy = cur = ListNode(next = head)

        for _ in range(m - n):
            cur = cur.next
            
        cur.next = cur.next.next
        return dummy.next