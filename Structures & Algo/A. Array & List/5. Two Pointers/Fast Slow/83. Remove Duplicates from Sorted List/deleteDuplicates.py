# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        
        l = head
        r = head.next
        
        while r:
            if l.val != r.val:
                l.next = r
                l = l.next
                
            r = r.next
        
        l.next = None
        
        return head


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        
        l = r = head
        
        while r:
            if l.val != r.val:
                l.next = r
                l = l.next
                
            r = r.next
        
        l.next = None
        
        return head