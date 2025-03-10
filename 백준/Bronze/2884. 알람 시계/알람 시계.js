let fs = require("fs");
let input = fs.readFileSync('/dev/stdin').toString().split("\n");

let h = Number(input[0].split(' ')[0])
let m = Number(input[0].split(' ')[1])

if (m < 45) {
  m += 60;
  m -= 45;
  h -= 1;
  if (h < 0) {
    h = 23;
  }
} else {
  m -= 45;
}

console.log(h, m);