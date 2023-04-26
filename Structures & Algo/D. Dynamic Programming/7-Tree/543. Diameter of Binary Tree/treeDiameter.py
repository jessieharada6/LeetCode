class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        print(graph)
        n = len(edges) + 1

        ans = 0
        def dfs(u, father) -> int:
            nonlocal ans
            cur_max_depth = 0
            for v in graph[u]:
                if v != father:
                    max_depth_v = dfs(v, u) + 1  #叶子结点到当前v点的当前深度
                    # print(v, u, max_depth_v, cur_max_depth)
                    ans = max(ans, max_depth_v + cur_max_depth) #求和,在cur_max_depth更新前，否则cur_max_depth会保留最深的深度从而求得一个更大的错误的和
                    cur_max_depth = max(cur_max_depth, max_depth_v) #当前max深度
                    # print(max_depth_v , cur_max_depth)
                    
            return cur_max_depth        
            
        
        depth = dfs(0, -1)
        return ans