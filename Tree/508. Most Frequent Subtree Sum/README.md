# 508. Most Frequent Subtree Sum

https://leetcode.com/problems/most-frequent-subtree-sum/

Use map to record: the value of each node, and the value of node plus the subtree sum
It is essential to return the sum, so the values are carried up onto the tree nodes
Use the map values to get the max count, remove any pair that does not have the same max count, and return the key in array format
