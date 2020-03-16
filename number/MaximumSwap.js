/**
 * @param {number} num
 * @return {number}
 */
const maximumSwap = num => {
  if (num <= 0) return;

  const numStr = String(num);
  // Biggest number from the right side, maximum number on each cell from the back
  const maxNum = new Array(numStr.length).fill(-1);
  maxNum[numStr.length - 1] = parseInt(numStr[numStr.length - 1]);

  for (let i = numStr.length - 2; i >= 0; i--) {
    maxNum[i] = Math.max(maxNum[i + 1], parseInt(numStr[i]));
  }

  // Find first instance of mismatch in array, this is the index to swap
  let indexToSwap = -1;
  for (let i = 0; i < numStr.length; i++) {
    if (maxNum[i] !== parseInt(numStr[i])) {
      indexToSwap = i;
      break;
    }
  }

  if (indexToSwap === -1) return num;

  // Find first number that matches the first index of mismatch from behind
  let secondIndexToSwap = 0;
  for (let i = numStr.length - 1; i >= 0; i--) {
    if (maxNum[indexToSwap] === parseInt(numStr[i])) {
      secondIndexToSwap = i;
      break;
    }
  }

  let newNum = '';
  for (let i = 0; i < numStr.length; i++) {
    if (i === indexToSwap) newNum += numStr[secondIndexToSwap];
    else if (i === secondIndexToSwap) newNum += numStr[indexToSwap];
    else newNum += numStr[i]
  }
  return parseInt(newNum);
};
