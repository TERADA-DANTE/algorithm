function solution(stones, k) {
  let [l, r, m] = [0, Math.max.apply(null, stones)]
  while (l <= r) {
    m = parseInt((l + r) / 2)
    if (isCrossable(stones, m, k)) {
      l = m + 1
    } else {
      r = m - 1
    }
  }
  return r
}

function isCrossable(array, n, k, cnt = 0) {
  for (let i of array) {
    n >= i ? cnt++ : (cnt = 0)
    if (cnt > k) return false
  }
  return true
}

console.log(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
