let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let a = Number(input[0]);
let sum =0

for (i=1;  i<=a; i++){
  sum+=i
}

console.log(sum)

