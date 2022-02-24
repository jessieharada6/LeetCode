# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# the key to this question is that we don't need to swap nodes
# but values, which makes this question quite approachable 
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        vals = []
        current = head
        
        while current:
            vals.append(current.val)
            current = current.next
        
        # vals = sorted(vals)
        vals.sort()
        
        current = head
        for i in range(len(vals)):
            current.val = vals[i]
            current = current.next
        
        return head
    