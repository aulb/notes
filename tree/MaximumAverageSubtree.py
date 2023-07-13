from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Node:
    value: int
    left: 'Node'
    right: 'Node'

class Solution:
    def maximumAverageSubtree(self, root: Optional[Node]):
        def traverse(root: Optional[Node]) -> List[int, int]: # node count, sum total
            if not root: return [0, 0]
            left_count, left_sum = traverse(root.left)
            right_count, right_sum = traverse(root.right)
            sum_so_far = root.value + left_sum + right_sum
            nodes_so_far = 1 + left_count + right_count
            nonlocal result
            result = max(sum_so_far / nodes_so_far, result)
            return [sum_so_far, nodes_so_far]
        traverse(root)
        result = 0
        return result
