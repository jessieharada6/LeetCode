# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        node1 = dummy1
        node2 = dummy2
        
        while head:
            if head.val < x:
                node1.next = head
                node1 = node1.next
            else:
                node2.next = head
                node2 = node2.next
            
            # temp = head.next
            # head.next = None
            # head = temp
            head = head.next
        
        # print(dummy1, dummy2)
        node1.next = dummy2.next
        # For this list: 5->6->1->2, x=3
        # at last cur2 points to 6, cur1 points to 2, 
        # we must set 6->1 to 6->null, otherwise there will be a cycle.
        node2.next = None
        return dummy1.next
        