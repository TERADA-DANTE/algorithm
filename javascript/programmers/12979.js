function solution(n, stations, w) {
  return stations.map((v) => [v - w, v + w])
  //   .reduce((pre, cur) => pre.concat(), [])
}

console.log(solution(16, [1, 2], 2))
