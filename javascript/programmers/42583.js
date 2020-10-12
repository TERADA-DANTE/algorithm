function solution(bridge_length, weight, truck_weights) {
  const [groups, trucks] = [[], (arr) => arr.reduce((a, b) => a + b, 0)]
  while (truck_weights[0]) {
    const group = []
    while (trucks(group) <= weight) group.push(truck_weights.shift())
    truck_weights.splice(0, 0, group.pop())
    groups.push(group)
  }
  return trucks(groups.map((v) => bridge_length + v.length - 1)) + 1
}

console.log(solution(2, 10, [7, 4, 5, 6]))
console.log(solution(100, 100, [10]))
console.log(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
//7 4 1 2 7
