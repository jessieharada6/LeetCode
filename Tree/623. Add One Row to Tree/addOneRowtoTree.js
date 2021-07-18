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
 * @param {number} val
 * @param {number} depth
 * @return {TreeNode}
 */

// Time complexity: O(n)
// Space complexity: O(1)
var addOneRow = function (root, val, depth) {
    if (depth === 1) {
        // let newRoot = new TreeNode(val);
        // newRoot.left = root;
        return new TreeNode(val, root);
    }

    let queue = [root];
    // let layer = 0;
    // let tempL, tempR;
    // let node = new TreeNode(val);

    while (queue.length) {
        let size = queue.length;
        // layer++;
        depth--;

        for (let i = 0; i < size; i++) {
            let current = queue.shift();
            // if (layer === depth - 1) {
            if (depth === 1) {
                // val as the current root, and the existing left subtree becomes the new node's left subtree
                current.left = new TreeNode(val, current.left);
                current.right = new TreeNode(val, null, current.right);
            }
            if (current.left) queue.push(current.left);
            if (current.right) queue.push(current.right);
        }
    }

    return root;
};