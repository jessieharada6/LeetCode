# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        path = ""
        if root is None: return "#"
        l = self.serialize(root.left)
        r = self.serialize(root.right)
        path = str(root.val) + "," + l + "," + r
        return path

    def deserialize(self, data):
        data = data.split(",")
        def dfs(data):
            val = data.pop(0)
            if val == "#": return None

            root = TreeNode(val)
            root.left = dfs(data)
            root.right = dfs(data)
            return root
        return dfs(data)

class Codec:
    def serialize(self, root):
        tree = ""

        def dfs(node, tree):
            if node is None: return "#" 
            
            l = dfs(node.left, tree)
            r = dfs(node.right, tree)
            tree = str(node.val) + "," + l + "," + r
            return tree

        return dfs(root, tree)
        
    def deserialize(self, data):
        data = data.split(",")
        print(data)

        def dfs(data):
            val = data.pop(0)
            if val == "#": return None 

            root = TreeNode(val)
            root.left = dfs(data)
            root.right = dfs(data)
            return root
        
        return dfs(data)


### Serialize and deserialize need to follow the same order
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        if root is None:
            # when deserialise, this is the none mark
            return "#"
        
        l = self.serialize(root.left)
        r = self.serialize(root.right)
        
        # print(str(root.val) + "," + l + "," + r)
        # pre-order, root, l, r
        # when deserialise - , is for split
        return str(root.val) + "," + l + "," + r 

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        # deserialise in the same order as serialisation
        d = data.split(",")
        
        def build(d):
            root_val = d.pop(0)
            if root_val is "#":
                return None
            
            root = TreeNode(root_val)
            root.left = build(d)
            root.right = build(d)
            # print(root)
            
            return root
        
        return build(d)
            
class Codec:
    def serialize(self, root):
        r = [] 
        q = [root]
        while q:
            node = q.pop(0)
            if node:                    # node not None
                r.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                r.append("#")
        
        return ",".join(r)
        
    def deserialize(self, data):
        print(data)
        if data == "#":
            return None
        
        d = data.split(",")
        
        c = 1
        root = TreeNode(d[0])
        q = [root]
        
        while c < len(d):
            node = q.pop(0)
            leftV = d[c]
            rightV = d[c + 1]
            
            if leftV != "#":
                n = TreeNode(leftV)
                node.left = n
                q.append(n)                     # next root
            if rightV != "#":
                n = TreeNode(rightV)
                node.right = n
                q.append(n)                     # next root
            c += 2                              # skip two none children
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0
        def traverse(root):
            nonlocal max_sum
            if root is None:
                return 1, inf, -inf, 0      
            
            is_l, min_l, max_l, sum_l = traverse(root.left)
            is_r, min_r, max_r, sum_r = traverse(root.right)
            
            if is_l and is_r and max_l < root.val < min_r:
                cur = sum_l + sum_r + root.val
                max_sum = max(cur, max_sum)
                min_l = min(min_l, root.val)
                max_r = max(max_r, root.val)
                return 1, min_l, max_r, cur
            else:
                return 0, 0, 0, 0
                
        traverse(root)
        return max_sum