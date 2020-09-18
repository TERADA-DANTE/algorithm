const fs = require("fs")
for (let i = 1004; i < 1050; i++) {
  fs.writeFile(`./${i}.py`, "", function (err) {
    if (err) return console.log(err)
    console.log(i, "done")
  })
}
