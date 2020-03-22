from queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any

# If the data elements are not comparable, the data can be wrapped in a class that ignores the data item and only compares the priority number:
@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = point = ListNode() # Common pattern, make dummy
        q = PriorityQueue()
        # O(logk) total addition
        for l in lists:
            if l:
                # A typical pattern for entries is a tuple in the form: (priority_number, data).
                q.put(PrioritizedItem(l.val, l))
        # O(n), getHighest is free
        # O(logk) per n
        while not q.empty():
            item = q.get()
            val = item.priority
            node = item.item
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put(PrioritizedItem(node.val, node))
        return head.next


#
# n = total element from all lists
# k = number of lists
# 1) Naive Solution: Grab all values from all lists, sort, make new linked list!
# Sort = nlogn
# Collecting and making linked list = n
# O(nlogn)

# 2) Compare one by one and make list
# Every iteration Math.min(k lists front)
# Go through n elements, every time make k comparisons to find smallest
# O(nk)

# 3) Priority queue: Solution above
# O(nlogk)
#
