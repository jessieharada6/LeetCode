# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = Counter()
        p = head
        while p:
            count[p.val] += 1
            p = p.next
        
        dummy = ListNode(-1)
        dummy.next = head
        q = dummy
        while q:
            unique = q.next
            while unique and count[unique.val] > 1:
                unique = unique.next

            q.next = unique
            q = q.next
                
        return dummy.next