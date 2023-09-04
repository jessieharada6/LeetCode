class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m, n, t = len(words), len(words[0]), len(target)
        mod = 10 ** 9 + 7
        cnt = [{} for _ in range(n)] # count occurences based on index
        for i in range(m):
            for j in range(n):
                ch = words[i][j]
                cnt[j][ch] = cnt[j].get(ch, 0) + 1
        # ["acca","bbbb","caca"] ->
        # [{'a': 1, 'b': 1, 'c': 1}, {'c': 1, 'b': 1, 'a': 1}, {'c': 2, 'b': 1}, {'a': 2, 'b': 1}]
        
        @cache
        def dfs(cur_idx, t_idx):
            if t_idx == t:
                return 1
            if n - cur_idx < t - t_idx:
                return 0
            
            if target[t_idx] not in cnt[cur_idx]: # target[i] != words[j][k]
                return dfs(cur_idx + 1, t_idx) 
            return (dfs(cur_idx + 1, t_idx)      # not select
                                                 # {'a': 2, 'b': 1} : * 2 because there are 2 a that match
                    + dfs(cur_idx + 1, t_idx + 1) * cnt[cur_idx][target[t_idx]]) % mod # select
        
        return dfs(0, 0)