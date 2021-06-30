/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var rob = function (root) {
    return Math.max(...dfs(root));
    function dfs(root) {
        if (!root) return [0, 0];

        let left = dfs(root.left);
        let right = dfs(root.right);

        let withRoot = root.val + left[1] + right[1];
        let withoutRoot = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);

        return [withRoot, withoutRoot];
    }
};