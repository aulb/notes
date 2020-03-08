/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
// O(N) count once
const kthSmallest = (root, k) => {
  if (!root) return;
  let number = 0;
  let count = k;

  // Counting ONCE
  const helper = node => {
    // Check left
    if (node.left) helper(node.left);
    // Count self
    count--;
    if (!count) {
      number = node.val;
      return;
    };
    // Start counting right
    if (node.right) helper(node.right);
  };

  helper(root);
  return number;
};

// // O(n^2), recursive, off by 1, k = 1 (means smallest)
// const kthSmallest = (root, k) => {
//   const countSmaller = countNodes(root.left);
//   // count === k === 1 > find smallest, and there is a node on the left
//   if (countSmaller >= k) return kthSmallest(root.left, k);
//   if (countSmaller + 1 < k) return kthSmallest(root.right, k - countSmaller - 1);
//   return root.val;
// };

// const countNodes = node => {
//   if (!node) return 0;
//   return 1 + countNodes(node.left) + countNodes(node.right);
// };
