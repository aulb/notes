/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
const invertTree = root => {
  if (!root) return root;

  const toVisit = [root];
  while (toVisit.length) {
    const node = toVisit.pop();
    // This swapping method does not work on LC
    // [root.left, root.right] = [root.right, root.left];
    const left = node.left;
    const right = node.right;
    node.left = right;
    node.right = left;
    if (node.left) toVisit.push(node.left);
    if (node.right) toVisit.push(node.right);
  }

  return root;
};
