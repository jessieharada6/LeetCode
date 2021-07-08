# 235. Lowest Common Ancestor of a Binary Search Tree

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

continuously look for the three conditions below

```
[6,2,8,0,4,7,9,null,null,3,5] p = 2, q = 4
```

at 3, p.val < root.val but q.val > root.val, so return root [3], same for at 5
at 4, p.val < root.val, q.val = root.val, so return root [4,3,5]
at 0, both greater, so return right null
at 2, p.val = root.val, q.val > root.val, so return root [2,0,4,null,null,3,5]
at root 6, p.val < root.val, q.val < root.val, so return left [2,0,4,null,null,3,5]

Not necessary to check if (!root), as it is BST and

- All Node.val are unique.
- p != q
- p and q will exist in the BST
