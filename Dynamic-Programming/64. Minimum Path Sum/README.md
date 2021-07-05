# 64. Minimum Path Sum

https://leetcode.com/problems/minimum-path-sum/

Don't think on the rows yet, always start with base case
Similar to the Unique Path,
To start with, the first row and first column are updated, as when we only have 1 row or 1 column, we have no other choice but to go right continuously or go down continuously
Then update each point based on the smallest values of the upper and left, in the order of left to right
In the end, update the entire grid
