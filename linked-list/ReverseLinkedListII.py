# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        def reverse(node, count):
            curr = node
            prev = None
            while count and curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                count -= 1
            node.next = temp
            return prev
        pos = 1
        curr = head
        prev = None
        while curr:
            if pos == m:
                prevNext = reverse(curr, n - m + 1)
                if prev and prev.next:
                    prev.next = prevNext
                    return head
                return prevNext
            else:
                prev, curr = curr, curr.next
                pos += 1
        return head
