class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        result = 0
        memo = defaultdict(int)
        
        @lru_cache(None)
        def traverse(index, target):
            nonlocal result
            if index == len(nums):
                if target == 0:
                    return 1            # base case
                return 0
            
            key = str(index) + "." + str(target)
            
            if memo[key]:
                return memo[key]
        

            result = traverse(index + 1, target + nums[index]) + traverse(index + 1, target - nums[index])
            memo[key] = result
            
            return result

        
        return traverse(0, target)


# time limit exceeded -    O(2^n) n is len(nums)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        result = 0
        
        # cannot add lru_cache(None)
        def traverse(index, target):
            nonlocal result
            if index == len(nums):
                if target == 0:
                    result += 1
                return
            
            target += nums[index]
            traverse(index + 1, target)
            target -= nums[index]
            
            target -= nums[index]
            traverse(index + 1, target)
            target += nums[index]
        
        traverse(0, target)
        return result