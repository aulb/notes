# Implement Queue Using Stacks
More straight forward than you think. Peek should do something extra for you.

# Implement Stack Using Queues
Also more straight forward, O(n) for one of the method is fine.

# Randomized Sets No Duplicates
A hashmap and an array would suffice. Hashmap index lookup. Removing would be the bulk of the work.
Remove:
1) Find the item to remove
2) If the item is already at the end, done. Just pop
3) If the item is in the middle, swap the last element with this item.
We actually do not need to swap. An overwrite would do and is faster.
4) DON'T FORGET TO CLEAR THE INDEX LOOKUP

We can also implement it with just a hashmap. I tried and it performed MUCH worse. 108ms vs 392ms.

# Randomized Sets WITH Duplicates
1) How to make a linearly related probability?
2) How to track multiple?

We can extend from the previous similar question by keeping track of their indices, popping and sorting them as we remove.
However notice that we don't have to sort. We just need to remove the current `self.nums.length -1` from the index list.
We can use set to easily track the indices instead, so we don't have to sort everytime we overwrite an element.
Just becareful if the last element is the same as the element you're trying to remove. Its the easier case but needs to be separated.

# Add and Search Data Structure
Trie. If '.', just look at all the current possible.

# Min Stack
Classic cracking question. Tradeoffs: if its not runtime elsewhere, its space, you can always save multiple things in an array etc.
