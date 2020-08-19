function solution(m = new Array(100).fill(undefined).map((_, i) => i + 1)) {
  const sumOfSquare = m.reduce((pre, cur) => pre + cur * cur, 0)
  const squareOfSum = Math.pow((100 * 101) / 2, 2)
  return Math.abs(sumOfSquare - squareOfSum)
}

console.log(solution())
