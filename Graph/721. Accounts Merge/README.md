# 721. Accounts Merge

https://leetcode.com/problems/accounts-merge/

- Union Find
    A simplified implementation of union find <br/>
    ```
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
    ```
    Using union to updates the roots, use find to add the emails to the same roots (owners) <br/>
    The clean implementation is done by https://leetcode.com/problems/accounts-merge/discuss/1084738/Python-The-clean-Union-Find-solution-you-are-looking-for <br/>
    But I modified based on the classic approach <br/>

- enumerate()
    ```
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

    for i, (name, *emails) in enumerate(accounts):
        print(i, name, *emails)

    # *unpack the rest of the arguments in the array
    >> 0 John johnsmith@mail.com john_newyork@mail.com
    >> 1 John johnsmith@mail.com john00@mail.com
    >> 2 Mary mary@mail.com
    >> 3 John johnnybravo@mail.com

    ```
    ```
    # normal call with separate arguments
    list(range(3, 6))            
    >> [3, 4, 5]

     # call with arguments unpacked from a list
    args = [3, 6]
    list(range(*args))           
    >> [3, 4, 5]
    ```