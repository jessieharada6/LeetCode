class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            visited.add(city)
            for sister in range(n):
                # if the cities are connected
                # and not in visited
                # check on the sister city
                if isConnected[city][sister] and sister not in visited:
                    dfs(sister)
        
        n = len(isConnected)
        output = 0
        visited = set()
       
        for city in range(n):
            # if the city not in visisted
            # it is a start for a new province
            # bring this city to dfs and check its sisters
            if city not in visited:
                output += 1
                dfs(city)
        
        return output