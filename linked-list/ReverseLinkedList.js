/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
// Do not use simultaneous assignment (wonky on lc), tricky to debug
// Be explicit first, simplify later
const reverseList = head => {
  let curr = head;
  let prev = null;
  let temp = null;
  while (curr) {
      temp = curr.next;
      curr.next = prev;
      [curr, prev] = [temp, curr];
  }
  return prev;
};
