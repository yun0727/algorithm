let fs = require("fs");
let input = fs.readFileSync("dev/stdin").toString().split("\n");

let length = Number(input[0]);
let a = Number(input[1].split(" ")[0]);
result = '';

for (i = 0; i < length; i++) {
  result += Number(input[i + 1].split(" ")[0]) + Number(input[i + 1].split(" ")[1])
  result += '\n'
  
}

console.log(result)