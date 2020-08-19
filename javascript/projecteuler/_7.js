function isPrime(arr, n) {
  for (let i = 1; i < arr.length; i++) {
    if (!(n % arr[i])) return false
  }
  return true
}

function solution(n, i = 4) {
  const primes = [null, 2, 3]
  while (primes.length < n + 1) {
    isPrime(primes, i) ? (primes.push(i), i++) : i++
  }
  return primes[primes.length - 1]
}

console.log(solution(10001))
