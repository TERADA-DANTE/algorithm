function solution(arr) {
  // 부랄정복!
  const cnt = { 0: 0, 1: 0 }
  const [isValid, partition, execute] = [
    (arr, n, i) =>
      i === n
        ? "⚡"
        : new Set(arr[i]).size == 1 && [...new Set(arr[i])][0] == arr[0][0]
        ? isValid(arr, n, i + 1)
        : false,
    (arr, n) =>
      [
        [0, 0],
        [0, n],
        [n, 0],
        [n, n],
      ].map((v) =>
        new Array(n)
          .fill("🔥")
          .map((_, i) => arr[v[0] + i].slice(v[1], v[1] + n))
      ),
    (arr, n) =>
      isValid(arr, n, 0)
        ? (cnt[arr[0][0]] += 1)
        : partition(arr, ~~(n / 2)).forEach((particle) =>
            execute(particle, ~~(n / 2))
          ),
  ]
  execute(arr, arr.length)
  return Object.values(cnt)
}
console.log(
  solution([
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
  ])
)
