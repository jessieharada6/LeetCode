class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # union-find
        # current parent recording
        par = [ i for i in range(len(edges) + 1)]
        # use it to find which element is root
        rank = [1] * (len(edges) + 1)
        
        def find(n):
            p = par[n]
            print(p, par[n], par[p])
            while p != par[p]:
                print("!=", p, par[p])
                # compression path
                par[p] = par[par[p]]
                p = par[p]
            
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            print("b", p1, p2)
            # same parents will result in redundant edge
            if p1 == p2:
                return False
            
            print(p1, p2, rank)
            
            if rank[p1] > rank[p2]:
                print(">", rank[p1], rank[p2])
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                print("<=", rank[p1], rank[p2], par[p1])
                par[p1] = p2
                print(p1, p2)
                rank[p2] += rank[p1]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
                


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [ i for i in range(len(edges) + 1)]
        ranks = [1] * (len(edges) + 1)
        
        def find(n):
            p = parents[n]
            
            while p != parents[p]:
                parents[p] = parents[parents[p]]
                p = parents[p] 
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return False
            
            if ranks[p1] > ranks[p2]:
                parents[p2] = p1
                ranks[p1] += ranks[p2]
            else:
                parents[p1] = p2
                ranks[p2] += ranks[p1]
            
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        