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


# 前后缀分解
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        # 以i結尾的最大子數組的和
        # @cache
        # def dfsEnd(i):
        #     if i < 0: return -inf
        #     return max(arr[i], arr[i] + dfsEnd(i - 1))

        # # 以i開頭的最大子數組的和
        # @cache
        # def dfsStart(i):
        #     if i == n: return -inf
        #     return max(arr[i], arr[i] + dfsStart(i + 1))

        # one_deletion = max(dfsEnd(i - 1) + dfsStart(i + 1) for i in range(n))
        # deletion = max(dfsEnd(i) for i in range(n))

        # return max(one_deletion, deletion)

        f = [-inf] + [0] * n
        g = [0] * n + [-inf]

        for i in range(1, n + 1):
            f[i] = max(arr[i - 1], arr[i - 1] + f[i - 1])
        
        for i in range(n - 1, -1, -1):
            g[i] = max(arr[i], arr[i] + g[i + 1])

        one_deletion = max(f[i] + g[i + 1] for i in range(n))
        deletion = max(f[i + 1] for i in range(n))
        return max(one_deletion, deletion)                