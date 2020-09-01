function solution(v, w) {
  const lim = 10
  const dp = new Array(5).fill(undefined).map((_) => new Array(lim + 1).fill(0))
  for (let s = 0; s <= lim; s++) {
    dp[1][s] = w[1] <= s ? v[1] : 0
  }
  for (let i = 2; i <= 4; i++) {
    for (let s = 1; s <= lim; s++) {
      if (s < w[i]) {
        dp[i][s] = 0
        continue
      }
    }
  }
}

console.log(solution([null, 10, 40, 30, 50], [null, 5, 4, 6, 3]))
//console.log(solution(10, [1, 2, 5]))
