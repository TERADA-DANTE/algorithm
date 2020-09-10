function solution(routes) {
  const route = routes.sort((a, b) => a[0] - b[0])
  return (
    route
      .slice(1)
      .reduce(
        (pre, cur) => [
          cur[0],
          cur[0] > pre[1] ? ((pre[2] += 1), cur[1]) : Math.min(cur[1], pre[1]),
          pre[2],
        ],
        [...route[0], 0]
      )[2] + 1
  )
}

console.log(
  solution([
    [-20, 15],
    [-14, -5],
    [-18, -13],
    [-5, -3],
  ])
)
