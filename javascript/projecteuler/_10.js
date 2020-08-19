function isPrime(arr, n) {
  for (let i = 0; i < arr.length; i++) {
    if (!(n % arr[i])) return
  }
  return true
}

function solution(i = 8) {
  const primes = [2, 3, 5, 7]
  while (1) {
    if (i >= 2000000) return primes.reduce((pre, cur) => pre + cur, 0)
    isPrime(primes, i) ? (primes.push(i), i++) : i++
  }
}

console.log(solution())
