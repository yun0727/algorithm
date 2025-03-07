let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let a = input[0]
let b = input[1]
let c = parseInt(b / 100); //4
let d = parseInt((b - c * 100) / 10); //5
let e = b - c * 100 - d * 10; //6

console.log(a * e);
console.log(a * d);
console.log(a * c);
console.log(a*e+10*(a*d)+ 100*(a*c))