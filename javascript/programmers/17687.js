function solution(n, t, m, p) {
  let [numbers, i, system] = [
    [],
    0,
    new Array(16)
      .fill(undefined)
      .map((_, i) => (i < 10 ? i : String.fromCharCode(i + 55))),
  ]
  let execute = (n, ll, result = []) =>
    n >= ll
      ? execute(parseInt(n / ll), ll, [system[n % ll], ...result])
      : [system[n % ll], ...result]
  do (numbers = numbers.concat(execute(i, n))), i++
  while (numbers.length < t * m)
  return numbers.reduce(
    (pre, cur, idx) => (idx % m === p - 1 ? pre + cur : cur),
    ""
  )
  // .filter((_, i) => (i % m === p - 1 ? "💋" : 0))
  // .slice(0, t)
  // .join("")
}

console.log(solution(16, 16, 2, 1))
