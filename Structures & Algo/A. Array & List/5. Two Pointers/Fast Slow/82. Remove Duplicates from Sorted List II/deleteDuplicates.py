# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p = dummy
        q = head
        
        while q:
            if q.next and q.next.val == q.val:
                while q.next and q.next.val == q.val:
                    q = q.next
                q = q.next
                if not q: p.next = None
            else:
                p.next = q
                p = p.next
                q = q.next
        
        return dummy.next
                
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
            return head
        
        while head and head.next and head.val == head.next.val:
            head = head.next
        head.next = self.deleteDuplicates(head.next)
        return head.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                val = cur.next.val
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        
        return dummy.next
        