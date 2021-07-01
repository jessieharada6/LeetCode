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
 * @return {string[]}
 */
var binaryTreePaths = function (root) {
    let paths = [];
    dfs(root, "", paths);
    return paths;

    function dfs(root, path, paths) {
        if (!root) return;

        if (!root.left && !root.right) {
            path += root.val;
            paths.push(path);
        }
        // add the path after the if statement 
        // so i don't need to slice the string 
        // e.g. path.slice(0, -2)
        path += root.val + "->";

        dfs(root.left, path, paths);
        dfs(root.right, path, paths);
    }
};