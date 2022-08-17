# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random
# random.random() # generate number between 0 and 1
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        res = -1
        index = 1
        cur = self.head
        
        while cur:
            if random.random() < (1 / index):
                # dont return here, 
                # as we need to give chance to every number, 
                # not just the first number that has satisfied this condition
                res = cur.val       
            cur = cur.next
            index += 1
        
        return res
        
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()