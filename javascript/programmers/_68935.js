function solution(n, numbers = []) {
  while (n) numbers.push(n % 3), (n = parseInt(n / 3))

  return numbers.reduce(
    (pre, cur, idx, arr) => pre + cur * Math.pow(3, arr.length - idx - 1),
    0
  )
}

console.log(solution(45))
console.log(solution(125))
