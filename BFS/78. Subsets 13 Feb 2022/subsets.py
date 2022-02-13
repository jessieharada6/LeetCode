# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        
        # BFS: 
        # base case is output having 1 element
        # iterate nums
        # within the current length of output
        # generate new subset based on each current element of subsets
        
        for num in nums:
            for i in range(len(subsets)):
                # use + to create a new list!
                subset = subsets[i] + [num]
                subsets.append(subset)
                
        return subsets
            
        
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        
        for num in nums:
            # for s in subsets in list comprehension
            # loops within the current length of subsets
            # it is different from 
            # for s in subsets:
            subsets += [s + [num] for s in subsets]
                
        return subsets
    

# append vs += 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        
        for num in nums:
            for i in range(len(subsets)):
                # i.e. subsets.append(subsets[i] + [num])
                subsets += [subsets[i] + [num]]
                # subsets += [subsets[i] + [num]]:
                # [[]] += [[1]]
                # [[], [1]] += [[2], [1, 2]]
                # [subsets[i] + [num]]:
                # [[] + [1]]
                # [[1] + [2]]
                
        return subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        
        for num in nums:
            for i in range(len(subsets)):
                subsets.append(subsets[i] + [num])
                
        return subsets
    
            
    