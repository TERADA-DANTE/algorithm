function solution(fi = [1, 2]) {
  while (1) {
    l = fi.length
    f = fi[l - 1] + fi[l - 2]
    if (f > 4000000) break
    fi.push(f)
  }
  return fi.reduce((pre, cur) => (cur % 2 ? pre : pre + cur), 0)
}

console.log(solution())
