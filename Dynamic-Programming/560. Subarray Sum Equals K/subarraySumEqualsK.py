class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
    # k = sum k = 2
    # 1, 2, 3
    # if 3 - 2 in map, meaning between 3 and 1, there is a k
    
        result = 0
        sum = 0
        map = {}
        map[0] = 1
        
        for num in nums:
            sum += num
            
            if (sum - k) in map:
                result += map[sum - k]
                
            if sum in map:
                map[sum] += 1
            else:
                map[sum] = 1
        
        
        return result