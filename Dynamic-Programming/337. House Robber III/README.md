# 213. House Robber III

https://leetcode.com/problems/house-robber-iii/

For any node, we can determine the situation of [withRoot, withoutRoot]
The base case is when there is no more node, we return [0, 0]

For withRoot value, it is the root value itself with the values of withoutRoot:
root.val + left[1] + right[1]
For withoutRoot value, it is the max value from the left subtree, and the max value from the right subtree:
Math.max(left[0], left[1]) + Math.max(right[0], right[1])
