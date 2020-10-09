function solution(number, k) {
  // 시간초과... => Python Okay
  const queue = number.split("")
  stack = [queue.shift()]
  while (k && queue.length) {
    const q = queue.shift()
    while (k && stack[stack.length - 1] < q && 8) {
      stack.pop()
      k -= 1
    }
    stack.push(q)
  }
  return (k ? stack.slice(0, stack.length - k) : stack.concat(queue)).join("")
}
console.log(solution("1924", 2))
console.log(solution("1231234", 3))
console.log(solution("4177252841", 4))
