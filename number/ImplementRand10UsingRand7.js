/**
 * The rand7() API is already defined for you.
 * var rand7 = function() {}
 * @return {number} a random integer in the range 1 to 7
 */
const rand10 = () => {
  let result = [Infinity, 1];
  const getNumber = A => A[0] + (A[1] - 1) * 7;
  while (getNumber(result) > 40) {
    result = [rand7(), rand7()];
  }
  return 1 + (getNumber(result) - 1) % 10;
};


// Available: randInt (1 - 6)
const RAND_INT_MAX = 6;
const randIntWithCapLesser = cap => {
  // cap = 3, there is a 3/6 chance of it getting rejected, then try again
  let number = randInt(); // 5, cap = 3
  if (number > cap) number = randInt();
  return number;
};

const randIntWithCap = cap => {
  if (cap < RAND_INT_MAX) return randIntWithCapLesser();
  if (cap === RAND_INT_MAX) return randInt();

  // determine the how many times we have to roll..
  let counter = 1;
  while (cap > RAND_INT_MAX ** counter++) counter++;

  // cap = 24 < 36 so we need to roll 2 times..., the combination will help us get the uniform
  // cap = 50 > 36, 50 < 216 so we need to roll 3 times...
  const max = cap * Math.floor((RAND_INT_MAX ** counter) / cap); // cap = 10, max = 40
  number = 0;
  // Examine result, determine if we need to try again or not
  while (number > max) {
    let roll = 0
    const result = [];
    while (roll < counter) {
      result.push(randInt());
      roll++;
    }
    number = getNumber(result);
  }

  return 1 + (number - 1) % cap; // To deal with zeroes
}

/** Help think..., cap = 10, counter = 2 (2 dimensional)
1  2  3  4  5  6 => where they are on the grid
7  8  9 10  1  2
3  4  5  6  7  8
9 10  1  2  3  4
5  6  7  8  9 10
*  *  *  *  *  * => reject these numbers
result param:
[1, 3] => row 1 col 3 number = 3
[5, 6] => row 5 col 6 number = 40
[6, 1] => number = 41
*/
const getNumber = result => {
  if (!result || !result.length) return 0;

  let number = result[0];
  for (let i = 1; i < result.length; i++) {
    number += (result[i] - 1) * RAND_INT_MAX * i; // 6, 36, 216...
  }
  return number;
}
