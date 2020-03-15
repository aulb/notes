/**
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */
const leastInterval = (tasks, n) => {
  if (!tasks) return 0;
  // Counter-ize the tasks, how many times are the tasks repeated
  const counter = {};
  // The number of most repeated task
  let majority = 0;
  // How many tasks are repeated `majority` # of times
  for (let task of tasks) {
    if (!counter[task]) counter[task] = 0;
    counter[task]++;
    majority = Math.max(majority, counter[task]);
  }

  let amountMajority = 0;
  for (let task of Object.keys(counter)) amountMajority += counter[task] === majority;

  // task array: [A, A, A, B, B, B, C, C, D, D]
  // cooldown = 1, 2, 3, 4: cooldown < unique(tasks)
  // A B C D A B C D A B C D A B is the fastest way
  // This is literally just the tasks, but rearranged

  // cooldown = 4, ... : cooldown >= unique(tasks)
  // A B C D i A B C D i A B C D i A B is the fastest way
  // 3 chunks of A B C D, and then leftover majority tasks

  // The key takeaway is that you don't have to order in a way such that
  // A B A B A B C D C D -> This is complicated
  // Think outside the box
  // Explanation: A B C D i (cooldown = 4), there are majority - 1 of these chunks of 5
  return Math.max(tasks.length, (majority - 1) * (n + 1) + amountMajority);
};
