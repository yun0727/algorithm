let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let length = Number(input[0]);
let scores = input[1].split(" ");

let MaxValue = scores.reduce((a, b) => Math.max(a, b));
let NewScores = [];
for (let i = 0; i < length; i++) {
  NewScores.push((scores[i] / MaxValue) * 100);
}

console.log(NewScores.reduce((a, b) => a + b) / length);
