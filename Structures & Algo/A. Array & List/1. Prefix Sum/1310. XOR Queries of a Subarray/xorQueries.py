class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = [0 for i in range(len(queries))]
        
        prefix = [0 for i in range(len(arr) + 1)]
        prefix[1] = arr[0]
        for i in range(1, len(arr)):
            prefix[i + 1] = prefix[i] ^ arr[i]
        
        for i, (l, r) in enumerate(queries):           
            res[i] = prefix[l] ^ prefix[r + 1]
        
        return res