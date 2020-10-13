function solution(strs, t) {
  // Python
  strs.sort((a, b) => b.length - a.length)
  const execute = (t, cnt) => {
    if (!t) return cnt
    for (let str of strs)
      str == t.slice(0, str.length)
        ? execute(t.slice(str.length), cnt + 1)
        : null
  }
  return execute(t, 0)
}

console.log(solution(["ab", "na", "n", "a", "bn"], "nabnabn"))
// 그리디 하게 DFS
// na => bn => ab => n
