let A = Number(lines.shift());
let B = Number(lines.shift());
let C = Number(lines.shift());
let areaTrianguloR = ((A*C)/2).toFixed(3);
let areaCirculo = (3.14159 * (C**2)).toFixed(3);
let areaTrapezio = (((A + B)*C)/2).toFixed(3);
let areaQuadrado = (B**2).toFixed(3);
let areaRetangulo = (A*B).toFixed(3);

console.log("TRIANGULO: "+areaTrianguloR+"\nCIRCULO: "+areaCirculo+"\nTRAPEZIO: "+ areaTrapezio+"\nQUADRADO: "+areaQuadrado+"\nRETANGULO: "+areaRetangulo);