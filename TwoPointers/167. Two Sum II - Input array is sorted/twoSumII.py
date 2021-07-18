# map
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(numbers):
            dict[numbers[i]] = i + 1
        
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in dict and dict[diff] != i:
                return [i + 1, dict[diff]]

# two pointers
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            if numbers[left] + numbers[right] < target:
                left += 1
            if numbers[left] + numbers[right] == target:
                break
        
        return [left + 1, right + 1]