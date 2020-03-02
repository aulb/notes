/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
const merge = intervals => {
  if (!intervals || !intervals.length) {
    return [];
  }

  if (intervals.length === 1) {
    return intervals;
  }

  // Assummed sorted by start. [start,end]
  // Sort the intervals by start if its not sorted
  // Assummed start > end always
  const sortedIntervals = intervals.sort((intA, intB) => intA[0] - intB[0]);
  let prevInterval = sortedIntervals[0];
  const mergedIntervals = [];
  for (let i = 1; i < sortedIntervals.length; i++) {
    const currInterval = sortedIntervals[i];
    // If the prev.end is >= curr.start, merge
    if (prevInterval[1] >= currInterval[0]) {
      // Take the highest end when merging
      prevInterval[1] = Math.max(prevInterval[1], currInterval[1]);
    } else {
      mergedIntervals.push(prevInterval);
      prevInterval = currInterval;
    }

    // Push the last one, return
    if (i === sortedIntervals.length - 1) {
      mergedIntervals.push(prevInterval);
    }
  }

  return mergedIntervals;
};
