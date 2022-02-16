# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:   
        head = ListNode(0)
        current = head
        carry = 0
        
        while l1 or l2:
            # l1 and l2 may be of different lengths 
            # iterate based on the longer length
            # check if l1 is None as it iterates to the next point
            #         ^
            # 9 9 9 9 None
            l1Val = l1.val if l1 is not None else 0
            l2Val = l2.val if l2 is not None else 0
            
            # sum from the starting point
            sumVal = l1Val + l2Val + carry
            # 18 / 10  - calculate the carry and add to the next sumVal
            carry = math.floor(sumVal / 10)
            # 18 % 10 - calculate current position
            sumVal = sumVal % 10
           
            # add current position to the next node
            current.next = ListNode(sumVal)
            # iterate our list
            current = current.next
            
            # iterate linked list
            if l1:
                l1 = l1.next
            if l2: 
                l2 = l2.next
        
        # check if there's carry left
        if carry > 0:
            current.next = ListNode(carry)
        
        return head.next
        