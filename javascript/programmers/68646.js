function solution(a) {
  let [l, r] = [
    a.reduceRight((pre, cur, idx, arr) => {
      let index = arr.slice(idx + 1).findIndex((v) => cur > v)
      return [index === -1 ? 0 : pre[index] + 1, ...pre]
    }, []),
    a.reduce((pre, cur, idx, arr) => {
      let index = arr
        .slice(0, idx)
        .reverse()
        .findIndex((v) => v < cur)
      return [...pre, index === -1 ? 0 : pre[idx - index - 1] + 1]
    }, []),
  ]
  return a.filter((_, i) => (!(l[i] && r[i]) ? "🔥" : null)).length
}
console.log(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
