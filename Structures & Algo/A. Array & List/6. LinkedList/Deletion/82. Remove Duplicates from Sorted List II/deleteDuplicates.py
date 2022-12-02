# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = Counter()
        cur = head
        while cur:
            counter[cur.val] += 1
            cur = cur.next
        
        dummy = cur = ListNode(next = head)
        while cur.next:
            val = cur.next.val
            if counter[val] > 1:
                while counter[val] - 1 >= 0:
                    cur.next = cur.next.next
                    counter[val] -= 1
            else:
                cur = cur.next
        
        return dummy.next