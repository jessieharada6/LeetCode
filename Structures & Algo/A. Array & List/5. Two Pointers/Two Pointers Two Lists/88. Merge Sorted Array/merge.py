class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m -= 1 
        n -= 1
        p = len(nums1) - 1
            
        while m >= 0 and n >= 0:
            if nums1[m] <= nums2[n]:
                nums1[p] = nums2[n]
                n -= 1
            else:
                nums1[p] = nums1[m]
                m -= 1
            p -= 1
        
        while n >= 0:
            nums1[p] = nums2[n]
            n -= 1
            p -= 1


# 方法1:
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 以nums1为主体
        # nums2与主体比较 

        arr = []
        j = 0
        
        # 到m为止 加入有效数字
        for i in range(m):
            while j < n and nums1[i] > nums2[j]:
                arr.append(nums2[j])
                j += 1
            arr.append(nums1[i])
        
        # 不用判断if j < n 因为如果j已经走完 就加一个空的数组进去
        arr += nums2[j:n]
        
        nums1[:] = arr

# 方法2:
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 平行主体 
        # 两个同是关照
        
        arr = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        
        arr += nums1[i:m]
        arr += nums2[j:]
        
        nums1[:] = arr