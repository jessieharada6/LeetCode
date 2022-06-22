# when there is no deadends
# repeating steps: 0000 -> 0001, 0001 -> 0000 --- dead loop

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        n = 4
        steps = 0
        q = collections.deque()
        q.append("0000")
        visited = [False for _ in range(n)]
        
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                print("cur", cur)
                if cur == target:
                    return steps
                for j in range(0, 4):              # len of lock is 4
                    print("j", j)
                    q.append(self.plusOne(cur, j))
                    q.append(self.minusOne(cur, j))
                        
            steps += 1
    
    def plusOne(self, cur, j):          # turn right
        newCur = ""
        if cur[j] == "9":
            newCur = "0"
        else:
            newCur = str(int(cur[j]) + 1)
        return cur[:j] + newCur + cur[j + 1:]
    
    def minusOne(self, cur, j):        # turn left
        newCur = ""
        if cur[j] == "0":
            newCur = "9"
        else:
            newCur = str(int(cur[j]) - 1)
        return cur[:j] + newCur + cur[j + 1:]
            


### first version - traditional BFS
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        n = 4
        steps = 0
        
        q = collections.deque()
        q.append("0000")
        
        ends = set()
        for d in deadends:
            ends.add(d)
            
        visited = set()
        visited.add("0000")
        
        while q:
            for i in range(len(q)):
                cur = q.popleft()

                if cur in ends:                 # exclude deadends
                    continue
                    
                if cur == target:
                    return steps
                
                for j in range(n):              # len of lock is 4
                    up = self.plusOne(cur, j)
                    if up not in visited:
                        q.append(up)
                        visited.add(up)
                    down = self.minusOne(cur, j)
                    if down not in visited:
                        q.append(down)
                        visited.add(down)
                        
            steps += 1
        
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
            
# remove ends set(), add the deadends to visited
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        n = 4
        steps = 0
        
        if "0000" in deadends:
            return -1
        
        q = collections.deque()
        q.append("0000")
        
        # ends = set()
        # for d in deadends:
        #     ends.add(d)
            
        visited = set()
        visited.add("0000")
        for d in deadends:
            visited.add(d)

        while q:
            for i in range(len(q)):
                cur = q.popleft()

#                 if cur in visited:              # exclude deadends
#                     print(cur)
#                     continue
                    
                if cur == target:
                    return steps
                
                for j in range(n):              # len of lock is 4
                    up = self.plusOne(cur, j)
                    if up not in visited:
                        q.append(up)
                        visited.add(up)
                    down = self.minusOne(cur, j)
                    if down not in visited:
                        q.append(down)
                        visited.add(down)
                        
            steps += 1
        
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
            
### another solution from Clarence-G

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        visited = set(deadends)
        if '0000' in visited:
            return -1
        q1 = set(['0000'])
        q2 = set([target])
        step = 0
        while q1 and q2:
            tmp = set()
            for curr in q1:
                if curr in q2:
                    return step
                if curr in visited:
                    continue
                visited.add(curr)
                for i in range(4):
                    for d in (-1, 1):
                        next = curr[:i] + str((int(curr[i]) + d) % 10) + curr[i + 1:]
                        tmp.add(next)
            step += 1
            q1 = q2
            q2 = tmp
        return -1