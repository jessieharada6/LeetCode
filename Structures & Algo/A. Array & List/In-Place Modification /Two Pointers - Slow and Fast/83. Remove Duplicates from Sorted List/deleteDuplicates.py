# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        slow = head
        fast = slow.next
        
        while fast:
            if slow.val != fast.val:
                slow = slow.next # slow pointer must move forward b/f updating the value
                slow.val = fast.val
            fast = fast.next
        
        slow.next = None
        return head

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        slow = head
        fast = slow.next
        
        while fast:
            if slow.val != fast.val:
                slow.next = fast # point to fast
                slow = slow.next # move slow to the new node that's now fast
            fast = fast.next
        
        slow.next = None
        return head