/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
const reorderList = head => {
  if (!head || !head.next) return;
  // Find middle
  const { middle } = severMiddle(head);
  // Reverse middle
  let reversedMiddle = reverseList(middle);
  // Intertwine one by one, head is guaranteed to have more than middle
  while (head) {
    const headNext = head.next;
    const middleNext = reversedMiddle ? reversedMiddle.next : null;
    head.next = reversedMiddle;
    if (reversedMiddle) reversedMiddle.next = headNext;

    head = headNext;
    reversedMiddle = middleNext;
  }
};

const severMiddle = head => {
  let slow = head;
  let fast = head;

  while (slow && slow.next && fast && fast.next && fast.next.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  const middle = slow.next;
  slow.next = null;
  return { head, middle };
};

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
  let temp = null;
  while (curr) {
      temp = curr.next;
      curr.next = prev;
      [curr, prev] = [temp, curr];
  }
  return prev;
};


/* Notice that Math.floor(length / 2).next is always null
length = 2 0,1         -> 0,1   // Special, just return
length = 3 0,1,2       -> 0,2,1
length = 4 0,1,2,3     -> 0,3,1,2
length = 5 0,1,2,3,4   -> 0,4,1,3,2
length = 6 0,1,2,3,4,5 -> 0,5,1,4,2,3

find middle
0,1,2,3,4,5 -> 0,1,2,null 3,4,5,null -> 0,1,2,null 5,4,3,null
0,5, 1,4, 2,3
head, middle

prevHeadNext = head.next;
prevMiddleNext = middle.next;

head.next = middle; 0->5 (middle)
middle.next = prevHeadNext; 5->1 (prevHeadNext)
*/
