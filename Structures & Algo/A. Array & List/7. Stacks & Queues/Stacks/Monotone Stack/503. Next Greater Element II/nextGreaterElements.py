class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = []
        res = [0 for _ in range(n)]

        # as array is circular, expand the length
        # 2,1,2,4,3 -> 2,1,2,4,3,2,1,2,4,3
        #                      ^ (updated here)
        for i in range(2 * n - 1, -1, -1): 
            # use modulus to get the index
            # the last element will get updated at the second time
            while s and s[-1] <= nums[i % n]: 
                s.pop()
            
            res[i % n] = s[-1] if s else -1
            s.append(nums[i % n])
            
            # print(i, i % n, s, nums[i % n], res)
        
        return res