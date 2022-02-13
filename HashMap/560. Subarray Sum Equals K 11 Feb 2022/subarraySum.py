class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output = 0
        
        # sum every element and store in the map
        # simultaneously - check if the current sum - k is in hashMap
        # if it is, the corresponding value is the number of ways we can get k 
        
        sum = 0
        hashMap = {}
        # prefix sum - 
        # initial situation
        # deal with the situation when the first number itself is equal to k
        hashMap[0] = 1
        
        for num in nums:
            sum += num
            
            # check before forming the next hashMap element so the scope wont be extended
            # (sum - k) shows the amount that needs to be chopped off
            # hashMap[sum - k]: number of ways to chop off the extra contiguous sum
            if (sum - k) in hashMap:
                output += hashMap[sum - k]
                
            hashMap[sum] = hashMap.get(sum, 0) + 1
            
        # print(hashMap)   
        return output
        
        