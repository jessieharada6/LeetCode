# permutations - unique elements but the same element can be chosen unlimited times

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        paths = []
        n = len(nums)
        
        def traverse(path):
            if len(path) == n:
                paths.append(path[:])
                return                  # base case, track up to the tree
            
            for i in range(n):
                path.append(nums[i])
                # print("before", i, path) # i is the index of the last num in the permutation
                traverse(path)
                # print("after", i, path)
                path.pop()
        
        traverse([])
        return paths