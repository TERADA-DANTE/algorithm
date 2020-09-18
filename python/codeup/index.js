const fs = require("fs")
for (let i = 1051; i < 1100; i++) {
  fs.writeFile(`./${i}.py`, "", function (err) {
    if (err) return console.log(err)
    console.log(i, "done")
  })
}
