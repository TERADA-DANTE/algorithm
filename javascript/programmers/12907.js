function solution(n, money) {
  const dp = money.reduce(
    (pre, cur) => ((pre[n - cur] = 1), pre),
    new Array(n + 1).fill(0)
  )
  function execute(i) {
    console.log(dp, i)
    if (dp[i]) return dp[i]
    // [1, 2, 5]
    dp[i] = money
      .filter((v) => i - v >= 0)
      .reduce((pre, cur) => pre + execute(i - cur), 0)
    return dp[i]
  }
  return execute(n)
}

console.log(solution(5, [1, 2, 5]))
//console.log(solution(10, [1, 2, 5]))
