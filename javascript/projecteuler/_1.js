function solution(m = []) {
  for (let i = 1; i < 1000; i++) {
    if (!(i % 3) || !(i % 5)) m.push(i)
  }
  return m.reduce((a, b) => a + b, 0)
}

console.log(solution())
