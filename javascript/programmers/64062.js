function solution(stones, k) {
  stones.push(Infinity)
  let stack = [{ count: Infinity, idx: -1 }]
  let answer = Infinity
  for (let i = 0; i < stones.length; i++) {
    console.log(stack, answer)
    const right = { count: stones[i], idx: i }
    while (stack[stack.length - 1].count < right.count) {
      const mid = stack.pop()
      const left = stack[stack.length - 1]
      if (right.idx - left.idx > k) {
        answer = Math.min(answer, mid.count)
      }
    }
    stack.push(right)
  }
  return answer
}

// function solution(stones, k) {
//   let [l, r] = [0, 200000000]
//   while (l <= r) {
//     let mid = parseInt((l + r) / 2)
//     isCrossable(stones, mid, k) ? (l = mid + 1) : (r = mid - 1)
//   }
//   return r + 1
// }

// function isCrossable(array, n, k, cnt = 0) {
//   for (let i of array) {
//     n >= i ? cnt++ : (cnt = 0)
//     if (cnt >= k) return false
//   }
//   return true
// }

console.log(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
