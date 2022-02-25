class UF:
    def __init__(self, n):
        # initially, every node is a root on its own
        self.roots = list(range(n))
    
    def find(self, x):
        while x != self.roots[x]:
            # right side: 
            # self.roots[x] and self.roots[self.roots[x]] should share the same root
            self.roots[x] = self.roots[self.roots[x]]
            x = self.roots[x]
        return x
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        
        if rootQ == rootP:
            return
        
        self.roots[rootP] = rootQ
    

# illustration based on example of accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # owners of the emails
        uf = UF(len(accounts))
        
        ownership = defaultdict(int)
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(ownership[email], i)
                ownership[email] = i
        
        # print(ownership)
        
        res = defaultdict(list)
        for email, owner in ownership.items():
            # owners (i.e.roots) from [0, 1, 2] to [1, 1, 2]
            res[uf.find(owner)].append(email)
        
        #print(res)
                
        res = [[accounts[owner][0]] + sorted(emails) for owner, emails in res.items()]
        return res                 