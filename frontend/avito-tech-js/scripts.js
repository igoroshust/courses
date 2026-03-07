let arr = [1, 2, 3, 4, 5, 6];
let arrBitSum = arr.slice(0, arr.length / 2).reduce((acc, item) => item + acc, 0);

console.log(arrBitSum);