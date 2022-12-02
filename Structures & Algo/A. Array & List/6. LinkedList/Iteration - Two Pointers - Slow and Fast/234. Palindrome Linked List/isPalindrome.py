# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = 0
        arr = []
        cur = head
        while cur:
            n += 1
            arr.append(cur.val)
            cur = cur.next
        
        l, r = 0, n - 1
        while l <= r:
            if arr[l] == arr[r]:
                l += 1
                r -= 1
            else:
                break

        if n % 2 and l - r == 2:
            return True
        if not n % 2 and l - r == 1:
            return True
        return False