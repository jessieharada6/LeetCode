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

        neighbour = [
            [1, 3],                 
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

        neighbour = [
            [1, 3],                 
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [1, 3, 5],
            [4, 2]
        ]
        
        ### double-sided BFS
        q1 = set()
        q2 = set()
        q1.add(current)
        q2.add(target)
        
        visited = set()
        visited.add(current)
        
        while q1 and q2:
            temp = set()
            
            for cur in q1:
                if cur in q2:
                    return steps
                
                visited.add(cur)
                
                # find the idx for "0"
                idx = 0
                for s in range(len(cur)):
                    if cur[s] == "0":
                        idx = s
                # print("idx", idx)
                
                for adj in neighbour[idx]:
                    new_cur = self.swap(cur, adj, idx)
                    if new_cur not in visited:
                        temp.add(new_cur)
            
            steps += 1
            q1 = q2
            q2 = temp
        
        return -1

    def swap(self, cur, adj, idx):
        cur = list(cur)
        for i in range(len(cur)):
            cur[adj], cur[idx] = cur[idx], cur[adj]
            break
        return "".join(cur) 