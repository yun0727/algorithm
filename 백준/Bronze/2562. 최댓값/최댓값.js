let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let data = input.map(x=> Number(x))

let max =Math.max(...data)



console.log(max);
console.log(input.indexOf(String(max))+1)
