const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const arr1 = input[1].trim().split(' ');
const arr2 = input[2].trim().split(' ');
let setArr = new Set(arr1.concat(arr2));
let intersection = arr1.length + arr2.length - setArr.size;
console.log(arr1.length + arr2.length - (2*intersection));