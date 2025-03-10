let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let a = Number(input[0]);


for (i=1;  i<=9; i++){
  console.log(a ,'*', i ,'=', a*i)
}
