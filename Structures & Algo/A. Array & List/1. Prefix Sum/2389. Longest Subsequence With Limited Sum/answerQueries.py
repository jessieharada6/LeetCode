class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        
        for i, q in enumerate(queries):
            queries[i] = bisect_right(nums, q)
        
        return queries