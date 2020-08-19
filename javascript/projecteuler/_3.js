function solution(n, i = 6000, m = []) {
  // Maximum stack size over => Manullay cover
  return n == 1
    ? m
    : n % i
    ? solution(n, i + 1, m)
    : solution(n / i, i, [i].concat(m))
}

console.log(solution(6857))
