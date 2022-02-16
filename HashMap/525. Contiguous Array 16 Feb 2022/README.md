# 525. Contiguous Array

https://leetcode.com/problems/contiguous-array/

- prefix sum
```
# this is for cases of [0, 1, 1, 1] 
# where the first two element is part of the contiguous array
# -1 as index starts from 0
# index 1 - (-1) = 2
nMap[0] = -1

for i in range(len(nums)):
    nMap[nSum] = i
```

- hash map to record the initial point 
```
# when the same sum appears
if nSum in nMap:
    output = max(output, i - nMap[nSum])
else:
    nMap[nSum] = i
```

- calculate distance of subarray
```
# i is the current end point
# nMap[nSum] is the initial point
# (initial point - current end point)

# when the same sum appears
if nSum in nMap:
    output = max(output, i - nMap[nSum])
```

- trick
```
# treat 0 as -1

for i in range(len(nums)):
    nSum += nums[i] if nums[i] == 1 else -1
```