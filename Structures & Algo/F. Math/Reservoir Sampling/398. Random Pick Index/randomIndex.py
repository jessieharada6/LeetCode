import random
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.index = defaultdict(list)
        for i, n in enumerate(self.nums):
            self.index[n].append(i)
        

    def pick(self, target: int) -> int:
        return random.choice(self.index[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


# TLE
import random
class Solution:
    
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        index, res = 1, -1
        for i, n in enumerate(self.nums):
            if n == target:
                if random.random() < 1 / index:
                    res = i
                index += 1
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)



# another interesting solution
# https://leetcode.com/problems/random-pick-index/discuss/699998/Python-Reservoir-sampling-solution
## RC ##
    ## APPROACH : RESERVOIR SAMPLING ##
    ## 1. If we already know size of the array, its simple, we can use random.choice() for all the indicies of that target and return. ( as random.choice has equal probability on all the indices )
    ## 2. What if the array size is not know, its infinite data set ?
    ## 3. Just like reservoir sampling, we maintain previous occurance count, say for [1,2,3,3,3] and target = 3, for i=2: we random int in the range 0 to 0, (prob = 1) when count = 2, random can in[0,1], prob =1/2, count = 3, random range = [0,2], prob = 1/3.
    
	## TIME COMPLEXITY : O(N) ##
	## SPACE COMPLEXITY : O(N) ##
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        res = None
        count = 0
        for i, x in enumerate(self.nums):
            if x == target:
                count += 1
                chance = random.randint(0, count - 1)
                # chance of getting 0 is 1/count, then we pick that number. So when we have 3 nums, chance of picking it is 1/3, (if chance is not 0, i value may be previous value or even previous before that. so prob remains 1/count)
                if chance == 0:
                    res = i
        return res