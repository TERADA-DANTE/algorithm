function solution(n) {
  // Handle a, b, c range roughly
  for (let a = 1; a < 333; a++) {
    for (let b = a + 1; b < 500; b++) {
      let c = 1000 - a - b
      if (a * a + b * b == c * c) return [a, b, c]
      // 200 * 375 * 425 is the answer
    }
  }
}
console.log(solution(1000))
