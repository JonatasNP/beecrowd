let nome = lines.shift();
let salarioFixo = Number(lines.shift());
let vendas = Number(lines.shift());
let comissao = vendas * 15/100;
let total = (salarioFixo + comissao).toFixed(2);
console.log("TOTAL = R$ " + total);