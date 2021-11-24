# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        
        remove_position = length - n
        print(remove_position)
        
        temp = head
        pre = temp
        for _ in range(remove_position):
            pre = temp
            temp = temp.next
        
        # temp is one element further from pre
        #print(pre, "temp", temp, "\n")
        
        # n = 1 and length = 1
        if remove_position == 0:
            head = head.next
        else:
            pre.next = temp.next
        
        return head