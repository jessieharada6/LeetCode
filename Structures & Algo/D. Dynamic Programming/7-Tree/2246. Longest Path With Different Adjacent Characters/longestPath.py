class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        for idx, pa in enumerate(parent):
            if pa != -1:
                graph[pa].append(idx) # rooted at node 0: directed
                # graph[idx].append(pa)

        ans = 0
        def dfs(u):
            nonlocal ans
            cur_max_depth = 0
            for v in graph[u]:
                max_depth_v = dfs(v) + 1
                if s[u] != s[v]: ### only check after getting max depth - 
                                 ### e.g. [-1,0,1] aab, a and a at node 1 and 2 won't be able to get in to the loop to check further
                    ans = max(ans, max_depth_v + cur_max_depth)
                    cur_max_depth = max(cur_max_depth, max_depth_v)
                    
            return cur_max_depth
        
        dfs(0)
        return ans + 1