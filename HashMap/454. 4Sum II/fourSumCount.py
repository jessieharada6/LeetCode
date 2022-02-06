# break it down so it is O(n^2)
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
# nums1[i] + nums2[j] = 0 - (nums3[k] + nums4[l])
# v1 + v2 = 0 - (v3 + v4)
# if hashMap[0 - (v3 + v4)] in hashMap
# output += hashMap[0 - (v3 + v4)]

# defaultdict vs dict
# https://www.educative.io/edpresso/learning-about-defaultdict-in-python
# The functionality of both dictionaries and defaultdict are almost same 
# except - defaultdict never raises a KeyError. 
# It provides a default value for the key that does not exists.
# print(dict(hashMap))

# safe with defaultdict
# if value of hashMap[v3 + v4] not exist, it is 0
# else it is the actual frequencies
# output += hashMap[0 - (v3 + v4)]
# print(v3 + v4, hashMap[v3 + v4])

# defaultdict
# no key error raised if no key
# default(int) denotes value to 0 if no key
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        hashMap = defaultdict(int)
        output = 0
        
        # 1. hashMap contains all possible sum of nums1 + nums2
        for v1 in nums1:
            for v2 in nums2:    
                hashMap[v1 + v2] += 1

        
        # 2. get the value via the key of (0 - (v3 + v4))
        for v3 in nums3:
            for v4 in nums4:
                output += hashMap[0 - (v3 + v4)]
        
        return output
                
        

# Normal Dictionary
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        hashMap = {}
        output = 0
        
        # 1. hashMap contains all possible sum of nums1 + nums2
        for v1 in nums1:
            for v2 in nums2:    
                # .get(key, if not exist provide a default value)
                # .get() returns value
                hashMap[v1 + v2] = hashMap.get(v1 + v2, 0) + 1

        
        # 2. get the value via the key of (0 - (v3 + v4))
        for v3 in nums3:
            for v4 in nums4:
                # hashMap.get(0 - (v3 + v4) returns value
                # if key in dictionary
                # using hashMap.get() is not key, it will not go into the loop
                output += hashMap.get(0 - (v3 + v4), 0)
        
        return output
                
        
        