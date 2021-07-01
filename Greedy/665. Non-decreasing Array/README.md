# 665. Non-decreasing Array

https://leetcode.com/problems/non-decreasing-array/

Non-decreasing => increasing array:
a particular number is either equal to or greater than the numbers in front of it

We only increase the count if the neighbouring numbers are in decreasing order:
i.e. nums[i] < nums[i - 1]

Two cases:

1. if the current number [i] is greater than or equal to the number before [i - 2]
   we need to bring nums[i - 1] down to be the same as nums[i], to avoid there is a future number that is less than or equal to than the current number
   - considering equal so that the three numbers can be a horizontal line
   - if i is 1, bring nums[i - 1] down as it is the starting point, it should be the smallest number
2. if the current number [i] is less than the number before [i - 2]
   we need to bring nums[i] up to be the same as nums[i - 1]

Useful links:
https://www.youtube.com/watch?v=Dxv_kCAYOk4
