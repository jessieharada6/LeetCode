class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(start, end): # -> constructed trees
            ans = []
            # print(start, end)
            if start > end:
                return [None]

            for mid in range(start, end + 1):
                lefts = dfs(start, mid - 1)
                rights = dfs(mid + 1, end)

                for left in lefts:
                    for right in rights:
                        root = TreeNode(mid, left, right)
                        ans.append(root)
            return ans
        return dfs(1, n)