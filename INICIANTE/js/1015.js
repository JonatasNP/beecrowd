let linha1 = lines.shift().split(" ");
let linha2 = lines.shift().split(" ");
let x1 = Number(linha1.shift());
let x2 = Number(linha2.shift());
let y1 = Number(linha1.shift());
let y2 = Number(linha2.shift());
let calculo = Math.sqrt((x2 - x1)**2 + (y2 - y1)**2);
console.log(calculo.toFixed(4));