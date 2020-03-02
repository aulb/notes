/**
 * @param {number} num
 * @return {number[]}
 */
const countBits = num => {
  const bits = [0];
  for (let i = 1; i <= num; i++) {
    // Odd number always have
    if (i % 2) bits.push(bits[i - 1] + 1);
    // Even number has the exact same amount of numbers since multiplying by 2 shifts the bit by one place.
    else bits.push(bits[i / 2]);
  }
  return bits;
};
