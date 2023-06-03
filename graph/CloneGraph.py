"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# We don't need deque here
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        clones = {node.val: Node(node.val, [])}
        q = [node]
        while q:
            currentNode = q.pop()
            currentNodeClone = clones[currentNode.val]

            # Set neighbors
            for neighbor in currentNode.neighbors:
                # Create clone if not yet created
                if clones.get(neighbor.val, None) is None:
                    clones[neighbor.val] = Node(neighbor.val, [])
                    # Only append to visit for the first time only
                    q.append(neighbor) # Need to create their children

                currentNodeClone.neighbors.append(clones[neighbor.val])
        return clones[node.val]