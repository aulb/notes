# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: return head
        odd = head
        even = head.next
        evenHead = even

        # 1 and 1->2 case, move as a box
        while even and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head

    # def oddEvenListMyWay(self, head: ListNode) -> ListNode:
    #     curr = head
    #     evenHead = head and head.next
    #     counter = 1
    #     while curr:
    #         temp = curr.next
    #         curr.next = curr.next and curr.next.next
    #         if temp and temp.next is None:
    #             if counter % 2:
    #                 curr.next = evenHead
    #             else:
    #                 temp.next = evenHead
    #             break
    #         else:
    #             curr = temp
    #             counter += 1
    #     return head
