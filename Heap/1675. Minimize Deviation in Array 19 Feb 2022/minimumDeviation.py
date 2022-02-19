class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # odd number
        #   can only be multiplied by 2 once
        #   once it becomes even, the number can only be divided
        # even number
        #   can be divided by 2 as many times 
        #   until it becomes an odd number 
        
        res = math.inf
        
        queue = []
        for num in nums:
            # 2 & 1 = 0, 3 & 1 = 1
            queue.append(num * -2 if num & 1 == 1 else -num) 
        
        # print(queue)
        maxV = max(queue)
        # print("max", maxV)
        
        heapq.heapify(queue)
        
        while True:
            current = heapq.heappop(queue)
            # print(current)
            
            res = min(res, maxV - current)
            if current & 1:
                break   
            # current >>= 1 -> current /= 2
            # current <<= 1 -> current *= 2
            current >>= 1
            maxV = max(maxV, current)
            heapq.heappush(queue, current)
        
        return res

                
                
                
            
        
       
        