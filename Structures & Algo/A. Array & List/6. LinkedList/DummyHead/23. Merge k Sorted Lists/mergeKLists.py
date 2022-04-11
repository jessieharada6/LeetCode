# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# min heap
from heapq import heappop, heappush

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # add to heap - min heap
        for l in lists:
            while l:
                heappush(heap, l.val)
                l = l.next
        
        # form linked list
        head, l = None, None
        while heap:
            val = heappop(heap)
            if head is None:
                head = ListNode(val)
                l = head
            else:
                l.next = ListNode(val)
                l = l.next
        
        return head


# merge 2 lists everytime 
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1, list2): # https://leetcode.com/problems/merge-two-sorted-lists/
            dummy = ListNode()
            p = dummy
            
            while list1 and list2:
                if list1.val <= list2.val:
                    p.next = list1
                    list1 = list1.next
                else:
                    p.next = list2
                    list2 = list2.next
                p = p.next
            
            p.next = list1 or list2
            return dummy.next

        # lists is an array which consists of a series of linkedlists
        if len(lists) == 0:
            return None
        
        while len(lists) >= 2:
            merged = []
            for i in range(0, len(lists), 2):
                merged.append(mergeTwoLists(lists[i], lists[i + 1] if i + 1 < len(lists) else None))
            lists = merged

        return lists[0]
                