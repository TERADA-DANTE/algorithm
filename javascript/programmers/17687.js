function solution(n, t, m, p) {
  let [numbers, i, system] = [
    [],
    0,
    new Array(16)
      .fill(undefined)
      .map((_, i) => (i < 10 ? i : String.fromCharCode(i + 55))),
  ]
  let sex = (n, boji, result = []) =>
    n >= boji
      ? sex(parseInt(n / boji), boji, [system[n % boji], ...result])
      : [system[n % boji], ...result]
  do (numbers = numbers.concat(sex(i, n))), i++
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
