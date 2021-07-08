/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
// Time Complexity: O(n)
// Space Complexity: O(1)
var isBalanced = function (root) {
    // []
    if (!root) return true;
    return dfs(root) !== null;

    function dfs(root) {
        if (!root) {
            // console.log("!root", root)
            return 0;
        }

        let left = dfs(root.left);
        let right = dfs(root.right);
        // console.log(root.val, left, right)

        // at subtree, when the height > 1, we get null
        // when we get to the root, we will get left is null or right is null
        // as at the subtree, we already get null
        // [1,2,2,3,null,null,3,4,null,null,4]
        // without left === null || right === null
        // the function will not return null but 1 
        // as Math.max(null, null) + 1 is 1
        if (Math.abs(left - right) > 1 || !left || !right) {
            // console.log("inside", root.val, left, right)
            return null;
        }

        return Math.max(left, right) + 1;
    }
};