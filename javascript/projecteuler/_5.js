function isDivisible(n) {
  for (let i = 1; i <= 20; i++) {
    if (n % i) return
  }
  return true
}
function solution(i = 1) {
  while (1) {
    if (isDivisible(i)) return i
    i++
  }
}

console.log(solution())
