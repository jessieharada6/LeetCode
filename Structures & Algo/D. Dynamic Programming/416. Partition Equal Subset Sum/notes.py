# time exceeded 

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2: return False
        
        cache = {}

        # start:起点
        # s:之前选的数的和
        # bool:可否让已选的数字形成sum(nums) - sum(path) == sum(path)或sum(nums) = 2 * sum(path)
        def dfs(start, s) -> bool:
            if s * 2 > total:
                return False 

            if start == n:
                # 语法不合
                # if total == s * 2:
                # return True
                # 写成:
                return s * 2 == total
            
            # print(cache, s)
            if (start,s) in cache:
                return cache[(start,s)]
            
            # 不需要了 因为之前已有判断
            # if start == n:
            #     return
            
            cur1 = dfs(start + 1, s + nums[start])
            cur2 = dfs(start + 1, s)
            cache[(start,s)] = cur1 or cur2
            return cur1 or cur2

        return dfs(0, 0)

# 2.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2: return False
        target = total // 2

        f = set()
        f.add(0)                        # dfs(0,0)

        for num in nums:
            cur_f = set()

            for s in f:
                cur_f.add(s)            # dfs(start + 1, s)
                cur_f.add(s + num)      # dfs(start + 1, s + nums[i])

            if target in cur_f:
                return True
            f = cur_f

        return False
