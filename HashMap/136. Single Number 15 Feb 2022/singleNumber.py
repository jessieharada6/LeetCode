# HashMap
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
            
        for key, value in hashMap.items():
            if hashMap[key] != 2:
                return key


# XOR
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output = 0
        for num in nums:
            output ^= num
        
        return output

    # xor: 
    # same elements -> 0
    # diff elements -> diff element other than 0

    # if the array is {2,1,4,5,2,4,1} then it will be like we are performing this operation
    # ((2^2)^(1^1)^(4^4)^(5)) => (0^0^0^5) => 5.