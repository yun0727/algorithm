let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let length = Number(input[0]);
let number = input[1].split("");
let sum=0
for (let i=0;i<length;i++){
  sum += Number(number[i])
}


console.log(sum );
