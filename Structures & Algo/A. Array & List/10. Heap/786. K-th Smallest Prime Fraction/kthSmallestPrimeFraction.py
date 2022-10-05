class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        
        for j in range(1, len(arr)):
            heappush(heap, (arr[0]/ arr[j], 0, j))
        
        for _ in range(k - 1):
            _, i, j = heappop(heap)
            
            if i + 1 < j:
                heappush(heap, (arr[i + 1]/arr[j], i + 1, j))
             
        _, i, j = heappop(heap)
        return [arr[i], arr[j]]
            