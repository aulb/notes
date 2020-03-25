# Top K Most Frequent in Array (Offline)
Make counter! Use k-size min heap to get the top k-sized elements. O(nlogk)
Make counter! Make buckets with size of the maximum frequency. Extract k elements backwards. O(n)

# Kth Largest Element in Array
Make k-size min heap. Keep putting the values larger than the top node. Runtime O(nlogk)
Selection sort. O(n)

# Find Median from Data Stream (Online)
So many different ways to solve it. My fave is using two heaps a min and a max heap.
A max heap to store the smaller half of the input
A min heap to store the larger half
Enforced property: Min heap needs to be the smaller of the two if need be
