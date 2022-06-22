# two-sided BFS
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        n = 4
        steps = 0
        
        q1 = set()
        q2 = set()
        q1.add("0000")
        q2.add(target)
        
        ends = set()
        for d in deadends:
            ends.add(d)
            
        visited = set()

        while q1 and q2:
            temp = set()
            
            for cur in q1:
                if cur in ends: continue
                if cur in q2: return steps
                
                visited.add(cur)
                
                for j in range(n):              # len of lock is 4
                    up = self.plusOne(cur, j)
                    if up not in visited:
                        temp.add(up)
                    down = self.minusOne(cur, j)
                    if down not in visited:
                        temp.add(down)
                        
            steps += 1
            q1 = q2
            q2 = temp
        
        return -1
    
    def plusOne(self, cur, j):          # turn right: 4 possibilities
        newCur = ""
        if cur[j] == "9":
            newCur = "0"
        else:
            newCur = str(int(cur[j]) + 1)
        return cur[:j] + newCur + cur[j + 1:]
    
    def minusOne(self, cur, j):        # turn left: 4 possibilities
        newCur = ""
        if cur[j] == "0":
            newCur = "9"
        else:
            newCur = str(int(cur[j]) - 1)
        return cur[:j] + newCur + cur[j + 1:]
            
            