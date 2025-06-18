let km = Number(lines.shift());
let l = Number(lines.shift()).toFixed(1);
let consumo = (km / l).toFixed(3);
console.log(consumo + " km/l");