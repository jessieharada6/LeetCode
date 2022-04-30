class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = r = 0
        while r < len(nums):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
            r += 1
        
        return l
        
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = fast = 0
        
        while fast < len(nums):
            if nums[fast] != val: # if nums[fast] != val, assign to nums[slow] and slow moves forward 
                nums[slow] = nums[fast]
                slow += 1
            fast += 1 # if nums[fast] == val, skip
        
        return slow

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[slow] == val:
                if nums[fast] != val:
                    nums[slow] = nums[fast]
                    nums[fast] = val
                    slow += 1
            else:
                slow += 1
            fast += 1
        
        return slow