// LCA
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root, p, q) {
    return dfs(root);

    function dfs(root) {
        if (!root) return null;
        let left = dfs(root.left);
        let right = dfs(root.right);

        if (p === root || q === root) {
            // console.log("p & q", p, q, root)
            return root;
        }

        if (left && right) {
            // console.log("left & right", left, right)
            return root;
        } else if (!left) {
            // console.log("right", left, right)
            return right;
        } else if (!right) {
            // console.log("left", left, right)
            return left;
        }
    }
};