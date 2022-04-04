class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def count(mid):
            total = 0
            count = 1                  # the entire array is divided once - base case
            for num in nums:
                if total + num <= mid: ## check if it's going to be greater
                    total += num
                else:
                    total = num
                    count += 1
            return count
            
        
        l, r = max(nums), sum(nums)
        while l < r:
            mid = l + (r - l) // 2  # current sum
            if count(mid) <= m:     # current sum may be too big, or just nice
                r = mid
            else:                   # current sum is too small, divide too many times
                l = mid + 1         
            # print(l, r, mid)
        return l

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def count(mid):
            total = 0
            count = 1                  # the entire array is divided once - base case
            for num in nums:
                if total + num <= mid: ## check if it's going to be greater
                    total += num
                else:
                    total = num
                    count += 1
            return count
            
        
        l, r = max(nums), sum(nums)
        while l < r:
            mid = l + (r - l) // 2  # current sum
            if count(mid) < m:      
                r = mid - 1
            elif count(mid) > m:    
                l = mid + 1   
            else:
                r = mid       
            # print(l, r, mid)
        return l

        
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def count(mid):
            total = 0
            count = 1                  
            for num in nums:
                if total + num <= mid:
                    total += num
                else:
                    total = num
                    count += 1
            return count
            
        
        l, r = max(nums), sum(nums)
        # search left bound
        # but when count(mid) < m, it means the current sum is too big, so max sum (r) must be smaller
        while l <= r:
            mid = l + (r - l) // 2  # current sum
            if count(mid) < m:     
                r = mid - 1
            elif count(mid) > m:                   
                l = mid + 1
            else:
                r = mid - 1
            
        return l
            
            