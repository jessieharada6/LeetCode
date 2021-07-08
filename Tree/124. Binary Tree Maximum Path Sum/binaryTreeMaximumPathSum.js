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
var maxPathSum = function (root) {
    // must be -Infinity, not 0, as it could be [-3]
    let max = -Infinity;
    dfs(root);
    return max;

    function dfs(root) {
        if (!root) return 0;
        let left = dfs(root.left);
        let right = dfs(root.right);

        // check max(root, max(root_to_left, root_to_right))
        let partialPathSum = Math.max(root.val, Math.max(left, right) + root.val);
        // check max(partialPathSum, root_to_left_and_right)
        let pathSum = Math.max(partialPathSum, root.val + left + right);
        // global variable to keep the max, max(pathSum, max)
        max = Math.max(pathSum, max);
        // console.log("dfs", left, right, root.val);

        // must return partialPathSum as it is one path (root to left or right, or root)
        // if we return pathSum, we need to go through nodes twice sometimes
        // [5,4,8,11,null,13,4,7,2,null,null,null,1]
        // we must return it so that the left and right values are brought up to the tree
        // same for 508. "in order for the sum to be carried up to the tree, it needs to return"
        return partialPathSum;
    }
};

/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxPathSum = function (root) {
    let sum = -Infinity;
    dfs(root);
    return sum;

    function dfs(root) {
        if (!root) return 0;
        let left = dfs(root.left);
        let right = dfs(root.right);

        let onePathSum = Math.max(root.val, Math.max(left, right) + root.val);
        let pathSum = Math.max(onePathSum, left + right + root.val);
        sum = Math.max(pathSum, sum);

        return onePathSum;
    }
};