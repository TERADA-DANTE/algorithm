function solution(n, money = money.sort((a, b) => a - b)) {
  return (
    new Array(money.length + 1)
      .fill(undefined)
      .map((_) => [1].concat(new Array(n).fill(0)))
      .reduce(
        (p, row, i) =>
          p.concat([
            i
              ? row.reduce(
                  (q, col, j) =>
                    q.concat(
                      !j
                        ? 1
                        : p[i - 1][j] +
                            ((q[j - money[i - 1]] || 0) % 1000000007)
                    ),
                  []
                )
              : row,
          ]),
        []
      )[money.length][n] % 1000000007
  )
}

console.log(solution(10, [5, 3, 7]))
