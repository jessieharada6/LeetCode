class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        l = 0
        r = n - 1
        ans = [0 for _ in range(n)]
        
        container = defaultdict(list)
        for i in range(n):
            container[nums2[i]].append(i)
        
        nums1.sort()
        # print(container, nums1)
        for i, num in enumerate(sorted(nums2, reverse=True)):
            # nums2 max vs nums1 max
            # if nums2 max < nums2 max: use nums1 max at that position
            # else: use nums1 min at that position
            if num < nums1[r]:
                ans[container[num][0]] = nums1[r]
                r -= 1
            else:
                ans[container[num][0]] = nums1[l]
                l += 1
            container[num].pop(0) # used 
        
        return ans
                
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # search left bound, but l needs to be m + 1 when <= 
        # because the question requires only greater than
        def leftBound(list, num):
            l = 0
            r = len(list) - 1
            while l <= r:
                m = l + (r - l) // 2
                if list[m] <= num:
                    l = m + 1
                else:
                    r = m - 1
            return l
        
        n = len(nums1)
        ans = []
        nums1.sort()
        for num in nums2:
            index = leftBound(nums1, num)
            
            if index == n: ## no found index, all nums in nums1 <= nums in nums2
                index = 0
            ans.append(nums1[index])
            nums1.pop(index) # len(nums1) shrinks
            n -= 1 # reduce length 
            
        
        return ans
        
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        match = defaultdict(list) # can be more than one match
        mismatch = []
        
        n = len(nums1)
        i = 0
        
        nums1.sort() # nums1.sorted() change nums1 
        for num in sorted(nums2): # sorted(nums2) won't change nums2
            while i < n and num >= nums1[i]:
                mismatch.append(nums1[i])
                i += 1
            if i < n:                 
                match[num].append(nums1[i])

            i += 1
        
        # print(match)
        # print(mismatch)
        # ans = []
        # for i in range(n):
        #     if nums2[i] in match:
        #         # for n in match[nums2[i]]:
        #         #     ans.append(n)
        #         ans.append(match[nums2[i]].pop())
        #     else:
        #         ans.append(mismatch.pop())
        
        return [(match[num] or mismatch).pop() for num in nums2]
        
            
            
            