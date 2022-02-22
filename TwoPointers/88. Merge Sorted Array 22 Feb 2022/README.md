# 88. Merge Sorted Array

https://leetcode.com/problems/merge-sorted-array/

- nums[:] creates a new array object vs. nums
```
nums = []
vals = nums
vals.append(1)

# both nums and vals point to the same reference
print(vals, len(vals), len(nums))
# [1], 1, 1
```

```
nums1 = []
vals1 = nums1[:]
vals1.append(1)

# nums1 and vals1 point to different reference 
# vals1 is a new list with the same values
# same as:
# vals1 = nums1.copy()
# vals1 = list(nums)
print(vals1, len(vals1), len(nums1))
# [1], 1, 0
```