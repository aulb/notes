/*
Given an array of meeting time intervals consisting of start and end times [s1, e1], [s2, e2], ... , determine if a person could attend all meetings.

For example,
Given [ [0, 30], [5, 10], [15, 20] ],
return false.
Runtime on the sorting O(nlogn).
*/
const start = 0;
const end = 0;
const canAttendAll = meetings => {
  if (!meetings || !meetings.length) return false;
  // Sort by start time
  const sortedMeetings = meetings.sort((a, b) => a[0] - b[0]);
  const prev = sortedMeetings[0];
  for (let i = 1; i < sortedMeetings.length; i++) {
    const curr = sortedMeetings[i];
    if (curr[start] < prev[end]) return false;
  }
  return true;
};
