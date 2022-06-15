class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        
        def traverse(start, path):
            if len(path) == k:
                combinations.append(path[:])
            
            for i in range(start, n + 1):
                path.append(i)
                traverse(i + 1, path)
                path.pop()
        
        traverse(1, [])
        return combinations