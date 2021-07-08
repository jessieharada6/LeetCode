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
var balanceBST = function (root) {
    let array = [];
    dfs(root);
    console.log(array)
    return buildTree(0, array.length - 1);

    // using binary search style to generate a BST tree
    function buildTree(l, r) {
        if (l > r) return null;
        let m = l + Math.floor((r - l) / 2);
        let root = new TreeNode(array[m]);
        root.left = buildTree(l, m - 1);
        root.right = buildTree(m + 1, r);
        return root;
    }

    // BST inorder (left root right) generates an ascending-ordered array 
    function dfs(root) {
        if (!root) return;

        dfs(root.left);
        array.push(root.val);
        dfs(root.right);
    }
};