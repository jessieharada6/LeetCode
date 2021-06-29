# 437.Path Sum III

https://leetcode.com/problems/path-sum-iii/

Using dfs() to check the targetSum when root is included, i.e. targetSum - root.val

Using pathSum() to check the targetSum without the root, i.e. targetSum

Calling pathSum() has two implications:

- checks if the current node value is the same as targetSum, based on the root that dfs() is calling
- enables the dfs() to start at each node (as pathSum() always goes into dfs() when being called), checks the node and its left and right subtree

If (!root) ensures that an empty tree will not cause runtime error
