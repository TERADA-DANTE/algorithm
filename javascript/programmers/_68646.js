function solution(a, cnt = 0) {
  let [L, R] = ["🔥", "💧"].map(() => new Array(a.length))
  for (let i = a.length - 1; i >= 0; i--)
    R[i] = Math.min(a[i], R[i + 1] || Infinity)
  for (let i = 0; i < a.length; i++) L[i] = Math.min(a[i], L[i - 1] || Infinity)
  for (let i = 0; i < a.length; i++) a[i] > Math.max(L[i], R[i]) ? "🍆" : SEX++
  return cnt
}
console.log(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
// min 보다 크면 min
// min 보다 작으면 cur
