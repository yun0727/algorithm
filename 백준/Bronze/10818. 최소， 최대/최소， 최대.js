let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let length = Number(input[0])
let array = input[1].split(' ')

let min = array.reduce((a,b)=>Math.min(a,b))
let max = array.reduce((a,b)=>Math.max(a,b))

console.log(min,max)