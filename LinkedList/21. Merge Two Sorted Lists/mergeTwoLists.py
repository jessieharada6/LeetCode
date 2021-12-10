# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # a new list    
        #  current as entry point, so can return current.next in the end      
        current = ListNode()
        # let node traverse, as they are object, when node updates, current will update
        # use node to traverse, so current can stay at beginning
        node = current
        
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            
            # traverse
            node = node.next
        
        node.next = list1 or list2
        
        # current.next is the new linkedlist
        return current.next
            