# 198. House Robber

https://leetcode.com/problems/house-robber/

Initially, we have robbed nothing, rob1 = 0, rob2 = 0, these are the base cases
When we arrive at the houses, we start to loop, the variable i plays a significant role which informs the legit house to rob currently
As the base cases show, we have 2 options, we either rob1 + nums[i], or we rob2; which ones to choose? we choose the current max.
Then we roll rob1 to the next position, and let rob2 to record the current max, till the end of the loop.
