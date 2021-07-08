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
 * @return {TreeNode}
 */
var convertBST = function (root) {
    // global var to update the values, start from 0
    let sum = 0;
    dfs(root);
    return root;

    function dfs(root) {
        if (!root) return 0;

        // in place update
        // only need to update the value
        dfs(root.right);
        sum += root.val;
        root.val = sum;
        dfs(root.left);
    }
};