# hashmap
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums)
        hashMap = {}
        
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        
        for num in nums:
            if hashMap[num] * 2 > size:
                return num


# one pass
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        output = 0
        
        for num in nums:
            if count == 0:
                output = num
            if output == num:
                count += 1
            else:
                count -= 1
        
        return output