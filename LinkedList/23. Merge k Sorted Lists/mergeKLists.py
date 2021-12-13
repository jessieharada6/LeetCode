# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        # when the len is 1, it is merged
        while len(lists) > 1:
            mergedLists = []
            # merge 2 everytime
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                # until reaching the end
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeLists(list1, list2))
            # update
            lists = mergedLists
        return lists[0]
    
    # https://leetcode.com/problems/merge-two-sorted-lists/
    def mergeLists(self, l1, l2):
        current = ListNode()
        node = current
        
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        
        node.next = l1 or l2
        return current.next