# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def findFromEnd(head, k):
            p1 = head
            p2 = head

            for _ in range(k):
                p1 = p1.next

            while p1:
                p1 = p1.next
                p2 = p2.next
            
            return p2
            
        dummy = ListNode(-1)
        dummy.next = head
        p2 = findFromEnd(dummy, n + 1)
        
        p2.next = p2.next.next

        return dummy.next