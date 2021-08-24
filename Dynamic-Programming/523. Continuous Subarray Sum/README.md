# 523. Continuous Subarray Sum

https://leetcode.com/problems/continuous-subarray-sum/

Useful links: https://leetcode.com/problems/continuous-subarray-sum/discuss/99499/Java-O(n)-time-O(k)-space

(a+(n*x))%x is same as (a%x)

in case of the array [23,2,6,4,7] 
the running sum: [23,25,31,35,42] 
the remainders: [5,1,1,5,0]

We got remainder 5 at index 0 and at index 3. That means, in between these two indexes we must have added a number which is multiple of the k

--------

1. Running sum from first element to index i : sum_i. If we mod k, it will be some format like : sum_i = k * x + modk_1
2. Running sum from first element to index j : sum_j. If we mod k, it will be some format like : sum_j = k * y + modk_2

If they have the same mod, which is modk_1 == modk_2, 
subtracting these two running sum we get the difference 
sum_i - sum_j = (x - y) * k = constant * k
the difference is the sum of elements between index i and j, and the value is a multiple of k