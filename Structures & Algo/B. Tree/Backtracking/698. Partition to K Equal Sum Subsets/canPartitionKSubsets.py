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
        if mod: return False
        if k > len(nums): return False
        
        nums.sort()
        
        bucket = [0] * (k + 1)
        used = 0
        memo = defaultdict(bool)
        
        def traverse(index, k, used):
            if k == 0:
                # print(bucket)
                return True
            
            if bucket[k] == target: # current bucket is full, start the next bucket, from index 0 of nums
                res = traverse(0, k - 1, used)
                memo[used] = res    # used num can't be repeated for the next bucket
                return res
            
            if used in memo:
                # print(memo)
                return memo[used]
            
            for i in range(index, len(nums)):       ### starting from index
                if (used >> i & 1) == 1: continue
                if bucket[k] + nums[i] > target: continue
                
                bucket[k] += nums[i]
                used |= 1 << i
                if traverse(i + 1, k, used): return True
                bucket[k] -= nums[i]
                used ^= 1 << i
                
                # sorting the num
                # current num can't satisfy the condition, next num of the same value can't either
                # if two num is the same, use the next num
                while i + 1 < len(nums) and nums[i + 1] == nums[i]: 
                    i += 1

            return False
  
        return traverse(0, k, used)