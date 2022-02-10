class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        output = 0
        
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        
        for key, value in hashMap.items():
            if k == 0:
                # [1, 1, 3, 4, 1] k = 0 -> output: 1
                if hashMap[key] > 1:
                    output += 1
            else:
                # [1, 1, 3, 4, 5] k = 2 -> output: 2
                if hashMap.get(key + k, 0) > 0:
                    output += 1
        
        return output