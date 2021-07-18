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
 * @return {number[][]}
 */
var levelOrderBottom = function (root) {
    let result = []
    if (!root) return result;
    let queue = [root]

    while (queue.length) {
        let size = queue.length;
        let layer = []
        for (let i = 0; i < size; i++) {
            let current = queue.shift();
            if (current.left) queue.push(current.left);
            if (current.right) queue.push(current.right);
            layer.push(current.val)
        }
        result.unshift(layer);
    }

    return result;
};