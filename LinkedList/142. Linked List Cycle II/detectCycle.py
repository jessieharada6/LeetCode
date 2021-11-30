# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # defect cycle
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # found cycle
            if fast == slow:
                break
        
        # no cycle
        if fast == None or fast.next == None:
            return None
        # learnt this way too - can replace line 21 and 22
        # else:
        #     return None
        
        # find meeting point
        fast = head
        while fast != slow:
            #essential for fast to move first
            fast = fast.next
            slow = slow.next
        
        return slow