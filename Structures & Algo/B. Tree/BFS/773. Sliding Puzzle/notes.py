class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        ### prep
        m = 2
        n = 3
        
        steps = 0
        
        target = "123450"
        current = ""
        
        for i in range(m):
            for j in range(n):
                current += str(board[i][j])

        # print(current) # 123405
        
        # static for 2 x 3 array
        # position: 1d index, array content: index's neightbours (up, down, left, right)
        neighbour = [
            [1, 3],                 # position
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [1, 3, 5],
            [4, 2]
        ]
        
        ### BFS
        q = collections.deque()
        q.append(current)
        
        visited = set()
        visited.add(current)
        
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                # print(cur, "cur")
                if cur == target:
                    return steps
                
                # find the idx for "0"
                idx = 0
                for s in range(len(cur)):
                    if cur[s] == "0":
                        idx = s
                # print("idx", idx)
                
                for adj in neighbour[idx]:
                    new_cur = self.swap(cur, adj, idx)
                    # print("new_cur", new_cur)
                    if new_cur not in visited:
                        visited.add(new_cur)
                        q.append(new_cur)
            
            steps += 1
        
        return -1

    def swap(self, cur, adj, idx):
        cur = list(cur)
        for i in range(len(cur)):
            cur[adj], cur[idx] = cur[idx], cur[adj]
            break
        return "".join(cur)