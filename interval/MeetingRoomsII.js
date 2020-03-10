/*
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,

Given [[0, 30],[5, 10],[15, 20]],
return 2.

Naive: Sort by end date. Get all the non overlapping sets. Runtime: O(n^2)

Solution by: https://www.programcreek.com/2014/05/leetcode-meeting-rooms-ii-java/
Modified to my style. Basically use min heap.
public int minMeetingRooms(int[][] intervals) {
  Arrays.sort(intervals, Comparator.comparing((int[] itv) -> itv[0]));
  if (size(intervals) < 1) return 0;

  PriorityQueue<Integer> heap = new PriorityQueue<>();
  heap.offer(intervals[0][1]);
  int count = 1;
  for (let i = 1; i < intervals.length;i++) {
    if (itv[0] >= heap.peek()) {
      heap.poll();
    } else {
      count++;
    }
    heap.offer(itv[1]);
  }

  return count;
}
*/
const start = 0;
const end = 0;
const getMinConferenceRooms = meetings => {
  // Implement using min heap.
};
