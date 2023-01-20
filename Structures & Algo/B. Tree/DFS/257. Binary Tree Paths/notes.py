# 反过来
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node) -> List[str]:
            if not node: return []
            if node.left is node.right:
                return [str(node.val)]
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            paths = []
            print(paths, "l", l, "r", r, node.val)
            
            for path in l + r:               # path是已经组好的
                print("path", path)
                # path += "->" + str(node.val) #新的node 归的时候加
                # paths += [path]
                path += "->" + str(node.val)   # 生成目前为止的路径
                paths.append(path)             # 这里可以用append因为paths会给l和r储存
            
            return paths # 每一次return paths是当前层的左路径和右路径。 在新的一轮中 paths会是[]-左路径和右路径由l和r存储。


        return dfs(root)

# 反转后再生成从上往下的路径
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node) -> List[List[str]]:
            if not node: return []
            if node.left is node.right:
                return [[str(node.val)]]
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            paths = []
            # print(paths, "l", l, "r", r, node.val)
            
            for path in l + r:               
                paths.append(path + [str(node.val)]) #path是已有路径 是数组

            return paths # 每一次return paths是当前层的左路径和右路径。 在新的一轮中 paths会是[]-左路径和右路径由l和r存储。

        ans = []
        for nodes in dfs(root):
            ans.append("->".join(nodes[::-1]))
        return ans