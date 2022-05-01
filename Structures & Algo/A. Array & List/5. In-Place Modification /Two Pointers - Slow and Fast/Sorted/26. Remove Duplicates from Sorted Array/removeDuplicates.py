class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        
        while fast < len(nums):
            if nums[slow] < nums[fast]: # if nums are diff, slow moves forward and gets fast
                slow += 1               # slow pointer must move forward b/f updating the value 
                                        # 1,2 => update to 1, 2
                                        # 1, 1, 2 => update to 1, 2, 2
                nums[slow] = nums[fast]
                
            fast += 1
            # print(slow, fast)
        
        return slow + 1