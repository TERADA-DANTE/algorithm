function solution(m, n, board) {
  const newBoard = board.map((v) => v.split(""))
  return findSquare(newBoard)
}

function findSquare(board) {
  board
    .reduce(
      (pre, cur, idx, arr) =>
        pre.concat(
          cur.reduce(
            (p, c, i) =>
              c &&
              c == arr[idx][i + 1] &&
              c == (arr[idx + 1] || new Array(i + 1))[i] &&
              c == (arr[idx + 1] || new Array(i + 1))[i + 1]
                ? p.concat([[idx, i]])
                : p,
            []
          )
        ),
      []
    )
    .forEach((v) => {
      board[v[0]][v[1]] = 0
      board[v[0]][v[1] + 1] = 0
      board[v[0] + 1][v[1]] = 0
      board[v[0] + 1][v[1] + 1] = 0
    })
  return board
}

console.log(
  solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])
)
