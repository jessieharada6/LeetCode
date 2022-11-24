class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, 0
        for x in nums:
            if x >= 0:
                break
            j += 1
        
        i = j - 1
        n = len(nums)

        arr = []
        while i >= 0 and j < n:
            a = nums[i] * nums[i]
            b = nums[j] * nums[j]
            if a < b:
                arr.append(a)
                i -= 1
            else:
                arr.append(b)
                j += 1
        
        while i >= 0:
            arr.append(nums[i] * nums[i])
            i -= 1
        while j < n:
            arr.append(nums[j] * nums[j])
            j += 1
            
        return arr
            
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 找到非负数
        i = 0
        for i, n in enumerate(nums):
            if n >= 0:
                break
        j = i - 1
        
        ans = []
        
        while j >= 0 and i < len(nums):
            if abs(nums[j]) < abs(nums[i]):
                ans.append(nums[j] * nums[j])
                j -= 1
            else:
                ans.append(nums[i] * nums[i])
                i += 1
        
        while j >= 0:
            ans.append(nums[j] * nums[j])
            j -= 1
        
        while i < len(nums):
            ans.append(nums[i] * nums[i])
            i += 1
        
        return ans

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 找到非负数
        i = 0
        for i, n in enumerate(nums):
            if n >= 0:
                break
        j = i - 1
        
        ans = []
        
        for idx in range(i, len(nums)):
            # 用while款着 不然会去加nums[idx]
            while j >= 0 and abs(nums[j]) < abs(nums[idx]):
                ans.append(nums[j] * nums[j])
                j -= 1

            ans.append(nums[idx] * nums[idx])
        
        while j >= 0:
            ans.append(nums[j] * nums[j])
            j -= 1
       
        return ans

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 已排序 
        
        # 特殊情况: 坑 - 只有一个数字 i会变成-1 unbound local error
        if len(nums) == 1:
            nums[0] = nums[0] * nums[0]       
            return nums
    
        arr = []    
        # 1. 找到分界点
        i, j = 0, 0
        while i < len(nums):
            if nums[i] < 0:
                i += 1
            else:
                break
        
        i = i - 1
        j = i + 1
        # print(i, j)
        
        # 2. 整理数据
        nums1 = []
        nums2 = []
        
        # 正数
        for r in range(j, len(nums)):
            nums1.append(nums[r] * nums[r])
        # 负数
        for l in range(i, -1, -1):
            nums2.append(nums[l] * nums[l])
        
        ################################################
        # 3. 以nums1为主体
        # 方法一
        # 用正数当成主体 包含0
        # 将负数带入
        
        # 坑：没有正整数
        if len(nums1) == 0:
            nums[:] = nums2
            return nums
        
        j = 0
        for i in range(len(nums1)):
            while j < len(nums2) and nums2[j] < nums1[i]:
                arr.append(nums2[j])
                j += 1
            arr.append(nums1[i])
        
        # 坑：负数数组值更高
        arr += nums2[j:]
        nums[:] = arr
        return nums

       ################################################
       # 3. 以nums1为主体
       # 方法二
       # 平行进行
        
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                arr.append(nums1[i]) 
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        
        arr += nums1[i:]
        arr += nums2[j:]
        nums[:] = arr
        return nums


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        i, j, p = 0, n - 1, n - 1
        
        while i <= j:
            a = abs(nums[i])
            b = abs(nums[j])
            if a < b:
                ans[p] = b * b
                j -= 1
            else:
                ans[p] = a * a
                i += 1
            
            p -= 1
        
        return ans
        


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        heap = []
        
        for n in nums:
            heappush(heap, n * n)
        
        while heap:
            ans.append(heappop(heap))
        
        return ans