const fs = require("fs");
const [N, ...COLORS] = fs.readFileSync("./10869.txt").toString().split("\r\n");

function getBest(origin, target) {
  return origin.map((v) => {
    s = target.filter((w) => w[0] != v[0]);
    return s[0][1] < s[1][1]
      ? [s[0][0], s[0][1] + v[1]]
      : [s[1][0], s[1][1] + v[1]];
  });
}
function solution(N, ...COLORS) {
  const [n, colors] = [+N, COLORS.map((v) => v.split(" ").map((w) => +w))];
  let initial = colors.shift().map((v, i) => [i, v]);
  return colors
    .reduce(
      (pre, cur) =>
        getBest(
          pre,
          cur.map((v, i) => [i, v])
        ),
      initial
    )
    .sort((a, b) => a[1] - b[1])[0][1];
}

console.log(solution(N, ...COLORS));
