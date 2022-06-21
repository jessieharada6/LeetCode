# Number selects bucket
# notes.py has more cutting tree technique
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, mod = divmod(sum(nums), k)
        if mod: return False
        if k > len(nums): return False
        
        bucket = [0] * k
        nums.sort(reverse=True)
        
        def traverse(index):
            if index == len(nums):
                return True
            
            for i in range(k):
                if bucket[i] + nums[index] > target:
                    continue
                
                if i > 0 and bucket[i] == bucket[i - 1]:
                    continue
                    
                bucket[i] += nums[index]
                if traverse(index + 1): return True
                bucket[i] -= nums[index]
            
            return False
        
        return traverse(0)

# bucket selects num
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, mod = divmod(sum(nums), k)
        if k > len(nums): return False
        if mod: return False
        
        n = len(nums)
        nums.sort()
        bucket = [0] * (k + 1)              # bucket = [0] * k
        memo = defaultdict(bool)
        
        def traverse(index, k, used):
            if k == 0:                      # if k == -1: 
                return True
            
            if bucket[k] == target:
                res = traverse(0, k - 1, used)
                memo[used] = res
                return res
            
            if used in memo:
                return memo[used]
            
            for i in range(index, n):
                if bucket[k] + nums[i] > target: continue
                if (used >> i & 1): continue
                
                used |= 1 << i
                bucket[k] += nums[i]
                if traverse(i + 1, k, used): return True
                bucket[k] -= nums[i]
                used ^= 1 << i
                
                while i + 1 < n and nums[i + 1] == nums[i]:
                    i += 1
            
            return False
        
        return traverse(0, k, 0)                # return traverse(0, k - 1, 0)

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, mod = divmod(sum(nums), k)
        if k > len(nums): return False
        if mod: return False
        
        n = len(nums)
        nums.sort()
        bucket = [0] * k
        memo = defaultdict(bool)
        
        def traverse(index, b, used):
            if b == k:
                return True
            
            if bucket[b] == target:
                res = traverse(0, b + 1, used)
                memo[used] = res
                return res
            
            if used in memo:
                return memo[used]
            
            for i in range(index, n):
                if bucket[b] + nums[i] > target: continue
                if (used >> i & 1): continue
                
                used |= 1 << i
                bucket[b] += nums[i]
                if traverse(i + 1, b, used): return True
                bucket[b] -= nums[i]
                used ^= 1 << i
                
                while i + 1 < n and nums[i + 1] == nums[i]:
                    i += 1
            
            return False
        
        return traverse(0, 0, 0)            # starting from 0
        