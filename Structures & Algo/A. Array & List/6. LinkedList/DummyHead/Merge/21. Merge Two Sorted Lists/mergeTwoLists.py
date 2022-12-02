# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        cur.next = list1 or list2
        return dummy.next


# Get intersection
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,4]
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(next = None)
        
        while list1 and list2:
            if list1.val < list2.val:
                list1 = list1.next
            elif list1.val > list2.val:
                list2 = list2.next
            else:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
                list2 = list2.next

        return dummy.next

# Get union
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,2,3,4]


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p = dummy           # need another variable to traverse dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            
            p = p.next
        
        if list1:
            p.next = list1
        
        if list2:
            p.next = list2
        
        return dummy.next 