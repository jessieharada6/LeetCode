class NumArray:
    preSum = []
    def __init__(self, nums: List[int]):
        self.nums = nums
        
        # preSum[0] = 0
        self.preSum = [0,]
        accuSum = 0
        
        for num in nums:
            accuSum += num
            # append starting from index 1
            self.preSum.append(accuSum)

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right + 1] - self.preSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)