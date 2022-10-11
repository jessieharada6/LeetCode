# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        
        while p1 != p2:
            if p1 is None:
                p1 = headB
            else:
                p1 = p1.next
            
            if p2 is None:
                p2 = headA
            else:
                p2 = p2.next
        
        return p1 # return p2 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        lenA = lenB = 0
        while p1:
            p1 = p1.next
            lenA += 1
        while p2:
            p2 = p2.next
            lenB += 1
        diff = abs(lenA - lenB)
        
        p1 = headA
        p2 = headB
        if lenA > lenB:
            for _ in range(diff):
                p1 = p1.next
        else:
            for _ in range(diff):
                p2 = p2.next
        
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1
        
            