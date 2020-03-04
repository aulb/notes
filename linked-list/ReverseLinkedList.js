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
const reverseList = head => {
  let curr = head;
  let prev = null;
  while (curr.next) [curr, curr.next, prev] = [curr.next, prev, curr]
  curr.next = prev; // Do the end
  return curr;
};
