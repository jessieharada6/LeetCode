class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob1 = 0
        rob2 = 0
        
        for num in nums:
            cur_max = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = cur_max
        
        return rob2
        