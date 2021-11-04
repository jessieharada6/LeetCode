# 95. Unique Binary Search Trees II

https://leetcode.com/problems/unique-binary-search-trees-ii/

# at each node as root, it is to find all combinations of trees
# based on the combinations, create new tree
# two edge cases, 
# if left > right -> null as it is BST, left < root < right
# if left == right -> leaf node 