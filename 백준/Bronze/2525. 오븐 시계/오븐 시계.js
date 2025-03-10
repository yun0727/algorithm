let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let h = Number(input[0].split(" ")[0]);
let m = Number(input[0].split(" ")[1]);
let time = Number(input[1]);

if (m + time >= 60) {
  h += Math.floor((m + time) / 60);
  m = (m + time) % 60;
} 
else {
  m += time;
}

if (h >= 24) {
  h -= 24;
}

console.log(h, m);
