class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = [False] * n
        paths = []
 
        # 不写start 且不在dfs(start + 1, visited, path + [nums[i]])或dfs(i + 1, visited, path + [nums[i]])
        # 完全ok的
        # 因为递归自己知道去下一层， 用start或者i是为了我们自己知道

        # for i in range(n) 这里不需要(start, n) 因为我们需要总是从全排列 而非避免重复的子集

        # visited 的作用是保证本条路径的元素不重叠 123而非112之类的
        def dfs(visited, path):
            if len(path) == n:
                paths.append(path)
                return
            
            for i in range(n):
                if visited[i]: continue
                visited[i] = True
                dfs(visited, path + [nums[i]])
                visited[i] = False
        
        dfs(visited, [])
        return paths


######

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        vis = [False] * len(nums)
        def dfs(path, i, vis):
            if i == len(nums):
                ans.append(path)
                return
            
            for j, x in enumerate(nums):
                if not vis[j]:
                    vis[j] = True
                    # i+1不会递归往下，递归本身会往下，
                    # 我们保存i是因为要知道层数找到什么时候返回
                    dfs(path + [nums[j]], i + 1, vis) 
                    vis[j] = False
            
        dfs([], 0, vis)
        return ans

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(i, path):
            if i == len(nums):
                ans.append(path)
                return
            
            for x in set(nums) - set(path):
                dfs(i + 1, path + [x])

        dfs(0, [])
        return ans

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visit = [False] * len(nums)
        path = []

        def dfs(i):
            if i == len(nums):
                ans.append(path[:])
                return None
            
            for j, x in enumerate(nums):
                if not visit[j]:
                    visit[j] = True
                    path.append(x)
                    dfs(i + 1)
                    path.pop()
                    visit[j] = False
            
        
        dfs(0)
        return ans



class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        paths = []
        # path = []
        n = len(nums)
        
        def traverse(nums, path):
            if len(path) == n:
                paths.append(path[:])
                return
            
            for i in nums:
                if i in path:
                    continue
                path.append(i)
                traverse(nums, path)
                path.pop()
            
        traverse(nums, [])
        
        return paths

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        paths = []
        n = len(nums)
        used = [0 for _ in range(n)]
        
        def traverse(path):
            if len(path) == n:
                paths.append(path[:])
                return                  # base case, track up to the tree
            
            for i in range(n):
                if used[i]: continue
                used[i] = True
                path.append(nums[i])
                # print("before", i, path) # i is the index of the last num in the permutation
                traverse(path)
                # print("after", i, path)
                path.pop()
                used[i] = False
        
        traverse([])
        return paths

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        paths = []
        n = len(nums)
        
        def traverse(nums, path):
            if len(path) == n:
                paths.append(path[:])
                return
            
            for i in nums:
                if i in path:
                    continue
                path.append(i)
                traverse(nums, path)
                path.pop()
            
        for i in nums:
            traverse(nums, [i])
        
        return paths

# https://leetcode.cn/problems/permutations/solution/hui-su-suan-fa-by-powcai-2/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        paths = []
        
        def traverse(path, nums):
            if not nums:
                paths.append(path[:])
                return
            
            for i in range(len(nums)):
                # print("before", nums[i], nums)
                traverse(path + [nums[i]], nums[:i] + nums[i + 1:])
                # print("after", nums[i], nums)
        
        traverse([], nums)
        return paths


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def dfs(s, path):
            if len(s) == 0:
                ans.append(path)
                return
            
            for x in s:
                dfs(s - {x}, path + [x])
        
        dfs(set(nums), [])
        return ans

        
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        arr = []
        path = []

        def dfs(idx):
            if len(idx) == 0:
                arr.append(path[:])
                return
            for i, j in enumerate(idx):
                path.append(nums[j])
                dfs(idx[:i] + idx[i + 1:])
                path.pop()

        dfs(tuple(range(n)))
        return arr
    