function solution(words) {
  obj = {}
  let i = 1
  while (1) {
    console.log(obj)
    for (let s of words) {
      obj[s.slice(0, i)] = [...(obj[s.slice(0, i)] || [])].concat(s)
    }
    i += 1
    if (i > 5) {
      break
    }
  }

  return obj
}

console.log(solution(["word", "war", "warrior", "world"]))

// 'w' : 4개

// 'wa' : 2개
// 'wo' : 2개

// 'war' : 2개
// 'wor' : 2개

// 'war' :L 탈출
// 'word' : 1개
