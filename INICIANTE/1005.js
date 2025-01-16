let A = Number(lines.shift()) * 3.5;
let B = Number(lines.shift()) * 7.5;
let media = (A + B)/11;
if (media > 10){
  media = 10;
}
console.log(`MEDIA = ${media.toFixed(5)}`);