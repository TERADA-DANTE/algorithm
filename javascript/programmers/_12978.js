function solution(N, road, K) {
  let [graph, isVisited] = [
    road.reduce(
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
    ),
    ["💎"].concat(new Array(N - 1).fill(undefined)),
  ]
  let SEX = () =>
    graph[0].reduce(
      (pre, cur, idx) => (!isVisited[idx] && cur < pre[0] ? [cur, idx] : pre),
      [Infinity, 0]
    )[1]
  while (SEX()) {
    let next = SEX()
    graph[next].forEach(
      (v, i) => (graph[0][i] = Math.min(graph[0][i], graph[0][next] + v))
    )
    isVisited[next] = "🌎"
  }
  return (
    graph[0].reduce((pre, cur, idx) => (idx && cur <= K ? pre + 1 : pre), 0) + 1
  )
}

console.log(
  solution(
    5,
    [
      [1, 2, 1],
      [2, 3, 3],
      [5, 2, 2],
      [1, 4, 2],
      [5, 3, 1],
      [5, 4, 2],
    ],
    3
  )
)
