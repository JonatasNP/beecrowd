let numero = parseInt(lines.shift());
let horas = parseInt(lines.shift());
let valor = Number(lines.shift());
let salario = valor * horas;
console.log("NUMBER = " + numero + "\nSALARY = U$ " + salario.toFixed(2));