class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        #prefix sum
        pre = list(itertools.accumulate(nums))
        s = sum(nums)
        #print(pre, s)
        
        # dictionary, initially, nothing
        pred = collections.defaultdict(int)
        # counter on prefix
        # Counter({2: 1, 1: 1, 3: 1})
        sufd = collections.Counter(pre)
        
        # can use pred[-1]
        # not include the last sum
        # as that mean everything is at left
        sufd[sum(nums)] -= 1
        
        # floor division //
        # count how many prefix sum meets s % 2 without using k
        if s % 2 == 0:
            ans = sufd[s // 2]
        
        for i in range(n):
            cur = 0
            
            # only change k if it's not the same
            # and if the new_sum % 2 == 0
            if nums[i] != k:
                # take in diff of k - nums[i]
                news = s + k - nums[i]
                if news % 2 == 0:
                    # left side: don't count the i at 0
                    # that means everything is at right side
                    if i > 0:
                        cur += pred[news // 2]
                
                    # right side:
                    # one of the number has been changed 
                    if i < n - 1:
                        cur += sufd[news // 2 - (k - nums[i])]
            
            # choose to use k or not
            ans = max(ans, cur)
            
            # update the prefix sum in the counter
            sufd[pre[i]] -= 1
            # update pred
            pred[pre[i]] += 1
        
        return ans
            
            
        
        