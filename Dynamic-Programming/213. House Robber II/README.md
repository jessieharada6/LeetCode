# 213. House Robber II

https://leetcode.com/problems/house-robber-ii/

We reuse the logic from House Robber problem:
Initially, we have robbed nothing, rob1 = 0, rob2 = 0, these are the base cases
When we arrive at the houses, we start to loop, the variable i plays a significant role which informs the legit house to rob currently
As the base cases show, we have 2 options, we either rob1 + nums[i], or we rob2; which ones to choose? we choose the current max.
Then we roll rob1 to the next position, and let rob2 to record the current max, till the end of the loop.

The only difference is that the head house and the tail house can't be robbed at the same time, meaning, we can use sliding window logic
For example, [1, 2, 3, 1]
For the first time, we check on [1, 2, 3]
For the second time, we check on [2, 3, 1]

When we return the final result, nums[0] is for edge case - for example, [1], when length is 1
This case will just nicely miss the num due to the window defined, and will return 0, if we do not check on nums[0].
