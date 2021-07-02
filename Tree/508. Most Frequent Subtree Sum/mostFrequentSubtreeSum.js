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
 * @return {number[]}
 */
var findFrequentTreeSum = function (root) {
    let map = new Map();
    dfs(root);

    const count = Math.max(...map.values());
    for (const [key, value] of map) {
        if (map.get(key) !== count) {
            map.delete(key);
        }
    }

    return [...map.keys()];

    function dfs(root) {
        if (!root) return 0;

        let left = dfs(root.left);
        let right = dfs(root.right);

        let sum = root.val + left + right;
        map.set(sum, (map.get(sum) || 0) + 1);
        return sum;
    }
};