class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        # @cache
        # def dfs(curIdx, delete):
        #     if curIdx < 0: return -inf

        #     if delete == 0:
        #         # 选/不选之前的数字
        #         return max(dfs(curIdx - 1, 0) + arr[curIdx], arr[curIdx]) 
            
        #     #删/不删当前的数+选之前，删(什么也没有)/不删当前的数+不选之前
        #     return max(dfs(curIdx - 1, 0), dfs(curIdx - 1, 1) + arr[curIdx], arr[curIdx]) 
        
        # return max(max(dfs(i, 1), dfs(i, 0)) for i in range(n))

        f = [[-inf] * 2] + [[0] * (2) for _ in range(n)]
        for curIdx in range(1, n + 1):
            for delete in range(2):
                
                if delete == 0:
                    f[curIdx][delete] = max(f[curIdx - 1][0] + arr[curIdx - 1], arr[curIdx - 1]) 
                else:
                    f[curIdx][delete] = max(f[curIdx - 1][0], f[curIdx - 1][1] + arr[curIdx - 1], arr[curIdx - 1]) 

        return max(max(f[i][1], f[i][0]) for i in range(1, n + 1))
                