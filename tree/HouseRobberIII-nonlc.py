from typing import List, Tuple, Optional
from collections import deque

class Node:
  def __init__(self, value: int):
    self.value = value
    self.children = []

  def add_child(self, node: 'Node') -> None:
    self.children.append(node)

  def __repr__(self):
    return f"${self.value}"

def rob_house(root: Optional[Node]) -> int:
  def check(node: Optional[Node]) -> Tuple[int, int]:
    if not node: return (0, 0)
    child_values = [check(child) for child in node.children]
    rob_current = node.value + sum([child_value[1] for child_value in child_values])
    skip_robbing = sum([max(child_value) for child_value in child_values])
    return (rob_current, skip_robbing)
  return max(check(root))

def create_binary_tree(values: List[int]) -> Node:
  # using n-ary API
  if not values: return 
  nodes = deque([Node(value) if value else None for value in values])
  root = nodes.popleft()
  nodes_to_process = deque([root])
  print(nodes, nodes_to_process)
  while nodes and nodes_to_process:
    current_node = nodes_to_process.popleft()
    print(nodes, nodes_to_process, current_node)
    ########## Can be cleaned up later ##
    if nodes:
      left = nodes.popleft() 
      if left:
        nodes_to_process.append(left)
        current_node.add_child(left)
    if nodes:
      right = nodes.popleft()
      if right:
        nodes_to_process.append(right)
        current_node.add_child(right)
    ########## Can be cleaned up later ##
  return root

def print_recursive(node: Node, parent: Optional[Node]) -> None:
  print(node, parent)
  for child in node.children:
    print_recursive(child, node)

if __name__ ==  "__main__":
  binary_tree = [100,1000,2,5,77,None,100] # ==> [$100, $1000, $2, $5, $77, None, $100]
  root = create_binary_tree(binary_tree)
  # print(root.value)
  # print_recursive(root, None)
  print(rob_house(root))

