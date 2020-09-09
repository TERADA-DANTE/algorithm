function solution(word, pages) {
  return pages
    .map((v) => [v.toLowerCase()])
    .map((v) => [
      ...v,
      v[0].match(/(?<=<meta property="og:url" content=").*(?="\/>)/s)[0],
    ])
    .map((v) => [
      ...v,
      v[0]
        .match(/(?<=<body>).*(?=<\/body>)/s)[0]
        .match(/[a-z]+/g)
        .map((v) => v.toLowerCase())
        .filter((v) => v == word.toLowerCase()).length,
    ])
    .map((v) => [
      ...v,
      v[0]
        .match(/(?<=<body>).*(?=<\/body>)/s)[0]
        .match(/(?<=<a href=").*(?=">)/g),
    ])
    .map((S, E, X) => [
      E,
      S[2] +
        X.reduce(
          (pre, cur) =>
            cur[3].includes(S[1]) ? pre + cur[2] / cur[3].length : pre,
          0
        ),
    ])
    .sort((a, b) => b[1] - a[1])[0][0]
}
// return pages.map(function(v, i) {
//   return {
//     url: v.match(/(?<=<meta property="og:url" content=").*(?="\/>)/s)[0],
//     general: this[i].filter((v) => v.length == word.length && RegExp(word, "i").test(v)).length,
//     links: this[i].filter((v) => RegExp(/<a href=".*/, "i").test(v)).map((v) => v.match(/(?<=<a href=").*(?=">)/)[0]),}},
// pages.map((v) => v.match(/(?<=<body>).*(?=<\/body>)/s)[0].match(/<a.*?<\/a>|[a-z]+/gi)))
// .map((v, i, a) => [i, v.general + a.reduce((pre, cur) => cur.links.includes(v.url) ? pre + cur.general / cur.links.length : pre, 0),])
// .sort((a, b) => b[1] - a[1])[0][0]}
console.log(
  solution("blind", [
    '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://a.com"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href="https://b.com"> Link to b </a>\n</body>\n</html>',
    '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://b.com"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href="https://a.com"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href="https://c.com"> Link to c </a>\n</body>\n</html>',
    '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://c.com"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href="https://a.com"> Link to a </a>\n</body>\n</html>',
  ])
)
