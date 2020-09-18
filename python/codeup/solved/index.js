const fs = require("fs")
const files = fs.readdirSync("./solved/")
files.forEach((file) => {
  const oldPath = `./solved/${file}`
  const newPath = `./solved/_${file}`
  fs.rename(oldPath, newPath, (err) => console.log(err))
})
