class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(numbers) - 1
        
        while lo < hi:
            s = numbers[lo] + numbers[hi]
            if s < target:
                lo += 1
            elif s > target:
                hi -= 1
            elif s == target:
                return [lo + 1, hi + 1]