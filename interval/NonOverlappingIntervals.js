/**
 * @param {number[][]} intervals
 * @return {number}
 * [[1,100],[11,22],[1,11],[2,12]] (can't use start time duh)
 */
const eraseOverlapIntervals = intervals => {
  const start = 0;
  const end = 1;
  if (!intervals || intervals < 2) return 0;

  const sorted = intervals.sort((intA, intB) => intA[end] - intB[end]);
  let overlaps = 1;
  let prev = sorted[0];
  for (let i = 1; i < sorted.length; i++) {
    const curr = sorted[i];
    if (curr[start] >= prev[end]) {
      overlaps++;
      prev = curr;
    }
  }
  return intervals.length - overlaps;
};
