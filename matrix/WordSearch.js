const directions = [[0,1], [0,-1], [1,0], [-1,0]];
const visited = '#';
const helper = (board, word, i, j) => {
  // Mismatch letter in the beginning, skip everything
  if (board[i][j] !== word[0]) return false;

  // No more word left after to find, then we found everything
  // [['a']] => condition above is true, and then here is also true
  if (!word.substr(1)) return true;

  board[i][j] = visited;
  for (let direction of directions) {
    const [newI, newJ] = [i + direction[0], j + direction[1]];
    if (newI >= 0 && newI < board.length && newJ >= 0 && newJ < board[0].length && helper(board, word.substr(1), newI, newJ)) return true;
  }

  board[i][j] = word[0];
  return false;
};

/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
const exist = (board, word) => {
  if (!board || !board.length || !board[0] || !board[0].length) return false;
  if (!word || !word.length) return false;

  const m = board.length;
  const n = board[0].length;
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (helper(board, word, i, j)) return true;
    }
  }
  return false;
};
