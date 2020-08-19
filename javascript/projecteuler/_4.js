function solution() {
  // O(N^2)
  // check the product of two 3-digit number if it is palindrom
  // if so, memo.
  // get the largest palidrome
  candidates = []
  for (let i = 999; i > 99; i--) {
    for (let j = 999; j > 99; j--) {
      if (isPalindrome(i * j)) candidates.push(i * j)
    }
  }
  return candidates.reduce((pre, cur) => (pre < cur ? cur : pre), 0)
}

function isPalindrome(n) {
  return n + "" === (n + "").split("").reverse().join("")
}

console.log(solution())
