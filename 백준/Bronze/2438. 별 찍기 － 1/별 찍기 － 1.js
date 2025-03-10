let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let a = Number(input[0]);
let result = ''

for (i=0;  i<a; i++){
  for (j=0; j<=i; j++){
    result += '*'
  }
  result += '\n'
}
console.log(result)
