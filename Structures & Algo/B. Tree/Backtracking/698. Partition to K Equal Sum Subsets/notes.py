# num chooses buckets
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, mod = divmod(sum(nums), k)
        
        if mod: return False
        if k > len(nums): return False      # each subset has at least one number
        nums.sort()
        while nums and target == nums[-1]:  # remove buckets 
            nums.pop()
            k -= 1
            
        bucket = [0 for _ in range(k)]
        nums.sort(reverse=True)             # descending, use larger number to fill in the bucket - efficiency
        
        def traverse(bucket, index, target):
            if index == len(nums):          # if index reaches the end, all num has been placed into the bucket
                return True
            
            # try to place num in each bucket
            for i in range(k):                          
                # try to add from the 1st bucket
                # if overfill, then to the next, and onwards
                if bucket[i] + nums[index] > target:    
                    continue                            # upcoming num overfills the current bucket
                
                # a same num is trying to place into bucket[i]
                # as it was placed in bucket[i - 1] - this has happened before
                if i > 0 and bucket[i] == bucket[i - 1]:                  
                    # print("in", i, index, bucket)     
                    continue                            # so continue to cut repeating trees
                
                bucket[i] += nums[index]
                # print(i, index, bucket)
                if traverse(bucket, index + 1, target): return True
                bucket[i] -= nums[index]
                
                ### another way to cut repeating trees
                # if bucket[i] == 0: break               # as the index did not reach the end of the len(nums)
                                                         # all is backtracked
                                                         # all buckets become 0
            
            return False                                 # if index did not reach len(nums)
        
        return traverse(bucket, 0, target)


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

### this version has time exceeds, but it is good to learn backtracking
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, mod = divmod(sum(nums), k)
        
        if k > len(nums): return False
        if mod: return False
        nums.sort()
        if nums[-1] > target:return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1
        
        bucket = [0] * k
        
        def traverse(bucket):
            if not nums:
                return True
            
            num = nums.pop()                # index + 1         manual traverse
            for i in range(k):
                if bucket[i] + num > target:
                    continue
                
                bucket[i] += num
                if traverse(bucket): return True
                bucket[i] -= num
            
            nums.append(num)                # index - 1         manual traverse
            
            return False
        
        return traverse(bucket)


### timeout without index as the starting point of the for loop
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, mod = divmod(sum(nums), k)
        if mod: return False
        if k > len(nums): return False
        
        nums.sort()
        
        bucket = [0] * (k + 1)
        used = 0
        memo = {}
        
        def traverse(index, k, used):
            if k == 0:
                return True
            
            if bucket[k] == target: # current bucket is full, start the next bucket, from index 0 of nums
                res = traverse(0, k - 1, used)
                memo[used] = res    # used num can't be repeated for the next bucket
                return res
            
            if used in memo:
                # print(memo)
                return memo[used]
            
            for i in range(len(nums)):
                if (used >> i & 1) == 1: continue
                if bucket[k] + nums[i] > target: continue
                
                bucket[k] += nums[i]
                used |= 1 << i
                if traverse(i + 1, k, used): return True
                bucket[k] -= nums[i]
                used ^= 1 << i
                
                while i + 1 < len(nums) and nums[i + 1] == nums[i]: # if two num is the same, use the next num
                    i += 1

            return False
  
        return traverse(0, k, used)



# [4,3,2,3,5,2,1]
# 4
# [1,2,3,4]
# 3
# [2,9,4,7,3,2,10,5,3,6,6,2,7,5,2,4]
# 7
# [3,9,4,5,8,8,7,9,3,6,2,10,10,4,10,2]
# 10
# [730,580,401,659,5524,405,1601,3,383,4391,4485,1024,1175,1100,2299,3908]
# 4