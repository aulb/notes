const peek = lookup => lookup && lookup[lookup.length - 1];

/**
 * @param {number[]} heights
 * @return {number}
 */
const largestRectangleArea = heights => {
  if (!heights || !heights.length) return 0;
  let maxArea = heights[0];
  const indices = [0];
  for (let i = 1; i < heights.length; i++) {
    const height = heights[i];
    let top = heights[peek(indices)];
    // If its greater or equal to, add
    if (height >= top) {
      maxArea = Math.max(height, maxArea);
    }

  }

  return maxArea;
};
