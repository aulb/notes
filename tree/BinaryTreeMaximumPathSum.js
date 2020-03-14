/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
const maxPathSum = root => {
  if (!root) return 0;

  let maxValue = null;
  const maxPathDown = node => {
    if (!node) return 0;
    // Another trick to essentially ignore l/r if they're dead weight
    const l = Math.max(0, maxPathDown(node.left));
    const r = Math.max(0, maxPathDown(node.right));
    // Work with all negative number because l and r gets 0d out, leaving node.val behind
    maxValue = typeof maxValue === 'number' ? Math.max(maxValue, l + r + node.val) : l + r + node.val;
    // This is the trick, we are only keeping ONE path
    return Math.max(l, r) + node.val;
  };

  maxPathDown(root);
  return maxValue;
};
