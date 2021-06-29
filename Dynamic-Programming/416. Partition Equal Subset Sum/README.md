# 416.Partition Equal Subset Sum

https://leetcode.com/problems/partition-equal-subset-sum/

If the half of the sum has residual, we definitely can't make two partitions equal to the subsum, so it is false.
Then we use a set to record all the possible sums of the elements, with the base case of 0. If the set has the target, then it is true, otherwise, false.
