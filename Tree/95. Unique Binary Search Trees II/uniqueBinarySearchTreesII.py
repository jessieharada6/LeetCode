# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(left, right):
            trees = []
            if (left > right):
                trees.append(None)
                return trees
            
            for root_val in range(left, right + 1):
                left_tree = dfs(left, root_val - 1)
                right_tree = dfs(root_val + 1, right)
                
                for l in left_tree:
                    for r in right_tree:
                        root = TreeNode(root_val)
                        root.left = l
                        root.right = r
                        trees.append(root)
            return trees
            
        
        return dfs(1, n)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(left, right):
            trees = []
            if (left > right):
                return [None]
            
            for root_val in range(left, right + 1):
                left_tree = dfs(left, root_val - 1)
                right_tree = dfs(root_val + 1, right)
                
                for pair in product(left_tree, right_tree):
                        root = TreeNode(root_val, pair[0], pair[1])
                        trees.append(root)
            return trees
            
        
        return dfs(1, n)




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(left, right):
            trees = []
            #null node
            if left > right:
                return [None]
            #leaf node
            if left == right:
                return [TreeNode(left)]
                # leaf = TreeNode(left)
                # trees.append(leaf)
                # return trees
            
            for root_val in range(left, right + 1):
                left_tree = dfs(left, root_val - 1)
                right_tree = dfs(root_val + 1, right)
                
                for pair in product(left_tree, right_tree):
                        root = TreeNode(root_val, pair[0], pair[1])
                        trees.append(root)
            return trees
            
        
        return dfs(1, n)