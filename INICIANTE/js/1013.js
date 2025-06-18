let a = Number(lines.shift());
let b = Number(lines.shift());
let c = Number(lines.shift());
let maiorAB = (a+b+Math.abs(a-b))/2;
let maiorC2 = (maiorAB+c+Math.abs(maiorAB-c))/2;

console.log(maiorC2+" eh o maior");