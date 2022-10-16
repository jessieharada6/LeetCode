class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        i, j, p = 0, n - 1, n - 1
        
        while i <= j:
            a = abs(nums[i])
            b = abs(nums[j])
            if a < b:
                ans[p] = b * b
                j -= 1
            else:
                ans[p] = a * a
                i += 1
            
            p -= 1
        
        return ans
        


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        heap = []
        
        for n in nums:
            heappush(heap, n * n)
        
        while heap:
            ans.append(heappop(heap))
        
        return ans