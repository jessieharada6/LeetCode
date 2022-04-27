# patience sorting:
# if the card is smaller than what's on the pile, place the card to the most left pile

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # sort w in ascending order, when w is the same, sort h in descending order
        envelopes.sort(key = lambda x: (x[0], -x[1])) 
        height = []
        for w, h in envelopes:
            height.append(h)

        def LIS(nums):
            n = len(nums)
            top = [0 for _ in range(n)]
            piles = 0
            for i in range(n):
                # search the most left smallest number on the top vs current number in the range
                l = 0                    # current pile, every search init as 0 
                r = piles                # possible future pile
                while l < r:
                    m = l + (r - l) // 2
                    if top[m] < nums[i]:  # found a larger number (the largest h < current number)
                        l = m + 1
                    else:
                        r = m
                        
                # a new pile is required, as a larger number is found 
                if l == piles:            
                     piles += 1              
                top[l] = nums[i]          

            return piles
        
        return LIS(height)

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def lengthOfLIS(nums):
            piles = 0
            top = [0 for _ in range(len(nums))]

            # r, piles move simultanously
            # top[l]: when the neighbour (top[m]) >= nums[i], replace the current top[l] to nums[i]
            # piles: when the neighbour (top[m]) < nums[i], piles increase by 1
            for i in range(len(nums)):
                l = 0
                r = piles
                while l < r:
                    m = l + floor((r - l) / 2)
                    if top[m] >= nums[i]:
                        r = m
                    else:
                        l = m + 1
                # print(l, r, piles, i, top)
                # loop exits when l == r
                # only when top[m] < nums[i], l == piles
                if l == piles:
                    # print(l, piles)
                    piles += 1
                top[l] = nums[i]
            # print(top)
            return piles
                
            
        envelopes.sort(key = lambda x : (x[0], -x[1]))  
        # print(envelopes)
        
        height = []
        for w, h in envelopes:
            height.append(h)
            
        # print(height)
        return lengthOfLIS(height)