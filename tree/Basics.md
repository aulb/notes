# Binary Trees 
Just a regular two child'd tree y'all.
When it be searchin it needs to obey the rule (left small, right big).

# Breadth First Search
- Good to find a "shortest path"
- Uses a queue
```
set all nodes to "not visited"
q = new Queue();
q.enqueue(initialNode)
while (q != empty) 
  x = q.dequeue();
  if (x not visited)
    set x to visited
    for every edge of x. call it y
      if y has not been visited
        q.enqueue(y)
```

# Depth First Search
- Tells us if a path even exists.
- Uses a stack instead