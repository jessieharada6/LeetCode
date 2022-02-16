# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: 
            return head
        
        dummy = ListNode(0, head)
        current = dummy
        
        # need to check current.next for the last node
        # where the object still has .next attribute
        # if only checking current.next.next
        # for the last node, there's no object remaining nor the .next attribute
        while current.next and current.next.next:
            # position nodes
            first = current.next
            second = current.next.next
            
            # update pointers
            current.next = second
            first.next = second.next
            second.next = first
                        
            # traverse 2 nodes ahead
            current = current.next.next
        
        return dummy.next