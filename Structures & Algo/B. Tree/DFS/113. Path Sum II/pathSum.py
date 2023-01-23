# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(node, path, targetSum):
            if node is None: return
            if node.left is node.right and targetSum - node.val == 0:
                ans.append(path + [node.val])

            # 在每一个节点生成一个新的path
            dfs(node.left, path + [node.val], targetSum-node.val)
            dfs(node.right, path + [node.val], targetSum-node.val)
        
        dfs(root, [], targetSum)
        return ans

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(node, targetSum, path):
            if node is None: return
            targetSum -= node.val
            path = path + [node.val]   # make a copy at each node

            if node.left is node.right and targetSum == 0:
                ans.append(path)
                return

            dfs(node.left, targetSum, path)
            dfs(node.right, targetSum, path)
            
        
        dfs(root, targetSum, [])
        return ans

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(node, targetSum, path, ans):
            if node is None: return
 
            targetSum -= node.val
            path.append(node.val)

            if node.left is node.right and targetSum == 0:
                ans.append([x for x in path]) # path.copy(), path[:]
                path.pop()
                return
            
            dfs(node.left, targetSum, path, ans)
            dfs(node.right, targetSum, path, ans)
            targetSum += node.val
            path.pop()

        dfs(root, targetSum, [], ans)
        return ans

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(node, path, targetSum):
            if node is None: return
            if node.left is node.right and targetSum - node.val == 0:
                path.append(node.val)
                ans.append(path[:]) # 只将结果复制 因为path即将被手动改变 
                # ans.append(path+[node.val]) 不可以 因为path还未记录叶子结点 在pop时会出现错误
                path.pop()

            path.append(node.val)
            dfs(node.left, path, targetSum-node.val)
            dfs(node.right, path, targetSum-node.val)
            path.pop()
        
        dfs(root, [], targetSum)
        return ans