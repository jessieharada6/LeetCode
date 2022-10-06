# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        dummy = head
        while dummy:
            dummy = dummy.next
            n += 1
        
        n = n // 2
        p1 = head
        
        for _ in range(n):
            p1 = p1.next
        
        return p1


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = p2 = head
        
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        
        return p1
        
        