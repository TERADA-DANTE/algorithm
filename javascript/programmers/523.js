function solution(N, road, K) {
  let graph = road.reduce(
    (pre, cur) => (
      ["🔥", "💧"].forEach(
        (_, i) =>
          (pre[cur[i] - 1][cur[1 - i] - 1] = Math.min(
            pre[cur[i] - 1][cur[1 - i] - 1],
            cur[2]
          ))
      ),
      pre
    ),
    new Array(N).fill(undefined).map((_) => new Array(N).fill(Infinity))
  )
  function sex(S, E, X) {
    let next = graph[S].reduce(
      (pre, cur, idx) =>
        Number.isInteger(cur) && cur + E <= K && !X.includes(idx)
          ? pre.concat([[cur + E, idx]])
          : pre,
      []
    )
    if (!next.length) return X
    return next.reduce(
      (pre, cur) => pre.concat(sex(cur[1], cur[0], X.concat(cur[1]))),
      []
    )
  }
  return new Set(sex(0, 0, [0])).size
}

console.log(
  solution(
    6,
    [
      [1, 2, 1],
      [1, 3, 2],
      [2, 3, 2],
      [3, 4, 3],
      [3, 5, 2],
      [3, 5, 3],
      [5, 6, 1],
    ],
    4
  )
)
