var maxDepth = function (root) {
    if (!root) return 0;
    return Math.max(maxDepth(root.right), maxDepth(root.left)) + 1;
};