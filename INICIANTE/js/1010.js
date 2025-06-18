let [cod1, num1, val1] = lines.shift().split(" ");
let [cod2, num2, val2] = lines.shift().split(" ");
console.log("VALOR A PAGAR: R$ " + (num1*val1 + num2*val2).toFixed(2));