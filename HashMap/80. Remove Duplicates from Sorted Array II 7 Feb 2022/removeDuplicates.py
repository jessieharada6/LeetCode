class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)
        output = 0
        
        # count frequency
        for num in nums:
            hashMap[num] += 1
        
        
        # eliminate the frequency > 2
        for key, value in hashMap.items():
            # remove the value that appears > 2 times
            while value > 2:
                value -= 1
                nums.remove(key)
            
            output += value
        
        return output


# Not my solution, seems smart
# if the condition can't enter, meaning there is a repetitoin
# i < 2 for the initial 2 elements
# n > nums[i-2] is true when a new element comes up, i is at the position of repetition there is it more than twice

# i - 2 is the max distance that we can have the same element
# i points to the latest "legal" element (i.e. each element is max of 2)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        
        for num in nums:
            if i < 2 or nums[i - 2] < num:
                nums[i]  = num
                i += 1
            # print(nums, i)  
        
        return i
           
