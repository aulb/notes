/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 * RECURSIVE, its enough to get the min/max value from one above
 */
const isBiggerThan = (node, value) => node ? node.val > value : true;
const isSmallerThan = (node, value) => node ? node.val < value : true;

const checkSelfBSTProp = root => {
  if (!root) return true;
  // Check self BST prop
  // Check all values are lower than maxVal
  // Check recursive left and right
  const { left, right, val } = root;
  const leftCheck = left ? val > left.val : true;
  const rightCheck = right ? right.val > val : true;
  return leftCheck && rightCheck;
};

const leftHelper = (root, maxVal) => {
  if (!root) return true;
  const { left, right, val } = root;
  const leftChildCheck = isSmallerThan(left, maxVal);
  const selfCheck = isSmallerThan(root, maxVal);
  const rightChildCheck = isSmallerThan(right, maxVal);
  const valCheck = leftChildCheck && selfCheck && rightChildCheck;
  return checkSelfBSTProp(root) && valCheck && leftHelper(left, val) && rightHelper(right, val);
};

const rightHelper = (root, minVal) => {
  if (!root) return true;
  const { left, right, val } = root;
  const leftChildCheck = isBiggerThan(left, minVal);
  const selfCheck = isBiggerThan(root, minVal);
  const rightChildCheck = isBiggerThan(right, minVal);
  const valCheck = leftChildCheck && selfCheck && rightChildCheck;
  return checkSelfBSTProp(root) && valCheck && leftHelper(left, val) && rightHelper(right, val);
};

const isValidBST = root => {
  if (!root) return true;
  const { left, right, val } = root;
  return checkSelfBSTProp(root) && leftHelper(left, val) && rightHelper(right, val);
};
