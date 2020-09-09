function solution(routes, cnt = 0) {
  routes.sort((a, b) => a[0] - b[0])
  let [L, R] = routes.shift()
  while (routes.length) {
    let [l, r] = routes.shift()
    if (l > R) {
      cnt += 1
      continue
    }
  }
}

console.log(
  solution([
    [-20, 15],
    [-19, -18],
    [-14, -5],
    [-16, -13],
    [-15, -5],
    [-18, -13],
    [-5, -3],
  ])
)
