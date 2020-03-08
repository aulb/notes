/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 * No duplicates values
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
const buildTree = (preorder, inorder) => {
  if (!inorder || !inorder.length) return null;
  const val = preorder.shift();
  const idx = inorder.indexOf(val);
  const root = new TreeNode(val);
  root.left = buildTree(preorder, inorder.slice(0, idx));
  root.right = buildTree(preorder, inorder.slice(idx + 1));
  return root;
};
