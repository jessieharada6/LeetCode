class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = 1
        sum_r = 0
        
        while n <= len(arr):
            for i in range(len(arr)):  
                if i + n <= len(arr):
                    sum_r += sum(arr[i: i + n])
            n += 2
        
        return sum_r