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

// diameter:
// distance between any two nodes
// may or may not pass through roots
var diameterOfBinaryTree = function (root) {
    let max = 0;
    dfs(root);
    return max;

    function dfs(root) {
        if (!root) return 0;

        let left = dfs(root.left);
        let right = dfs(root.right);

        // max left (node1) and max right (node2) of the current node
        // diameter
        max = Math.max(max, left + right);
        // height of max left or right subtrees
        return Math.max(left, right) + 1;
    }
};