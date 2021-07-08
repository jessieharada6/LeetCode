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
// Time complexity: O(n)
// Space complexity: O(1)
var lowestCommonAncestor = function (root, p, q) {
    if (!root) return null;

    let left = lowestCommonAncestor(root.left, p, q);
    let right = lowestCommonAncestor(root.right, p, q);

    if (p === root || q === root)
        return root;

    // p === left && q === right || p === right && q === left
    if (left && right) {
        return root;
        // no nodes left at the current left subtree at all 
    } else if (!left) {
        return right
        // no nodes left at the current right subtree at all 
    } else if (!right) {
        return left;
    }
};


/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
// Time complexity: O(n)
// Space complexity: O(1)
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