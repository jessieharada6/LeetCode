class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # A. 
        # build list in form of [[val, index], [val, index]...] 
        # in ascending order based on val
        orders = [] 
        for index, num in enumerate(nums):
            for el in num:
                orders.append([el, index])        
        orders.sort(key = lambda x : x[0])        
        # print(orders)
        
        # B.sliding window
        # count if the current min/max covered at least 1 element each in each index
        res = []
        count = defaultdict(int)
        k = len(nums)
        # left: current starting
        left = 0
        # right: current ending - index updating by the loop
        for right, num in enumerate(orders):
            count[num[1]] += 1
            while len(count) == k:                
                # res is empty or find a smaller range
                if not res or res[1] - res[0] > orders[right][0] - orders[left][0]:
                    res = [orders[left][0], orders[right][0]]
                
                count[orders[left][1]] -= 1
                if count[orders[left][1]] == 0:
                    count.pop(orders[left][1])
                
                # update pointer
                left += 1
        
        return res