from typing import List
import collections
import itertools
import functools
import math
import string
import random
import bisect
import re
import operator
import heapq
import queue

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for r, num in enumerate(nums):
            if target - num in d:
                return [d[target-num], r]
            d[num] = r


# pointers
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = sorted(zip(nums, range(len(nums))))
        
        l, r = 0, len(nums) - 1
        while l < r:
            s = d[l][0] + d[r][0]

            if s == target:
                return [d[l][1], d[r][1]]
            
            if s < target:
                l += 1
            else:
                r -= 1

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().twoSum(nums=[2, 7, 11, 15], target=9), [0,1], "[0, 1]")
        self.assertEqual(Solution().twoSum(nums=[2, 7, 11, 15], target=18), [1, 2], "[1, 2]")

if __name__ == "__main__":
    unittest.main()

# print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
# print(Solution().twoSum(nums=[2, 7, 11, 15], target=18))
# print(Solution().twoSum(nums=[2, 7, 11, 15], target=22))