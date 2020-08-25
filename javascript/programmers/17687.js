function solution(n, t, m, p) {
  let [numbers, i] = [[], 0]
  do (numbers = numbers.concat(sex(i, n))), i++
  while (numbers.length < t * m)
  return numbers
    .filter((_, i) => (i % m === p - 1 ? "💋" : 0))
    .slice(0, t)
    .join("")
}

function sex(n, boji, result = []) {
  const system = new Array(boji)
    .fill(undefined)
    .map((_, i) => (i < 10 ? i : String.fromCharCode(i + 55)))
  return n >= boji
    ? sex(parseInt(n / boji), boji, [system[n % boji], ...result])
    : [system[n % boji], ...result].map((v) => [v])
}
