const arr = [1, 2, 3, 3, 5];

const result = arr.reduce((acc, i) => acc.find(item => item === i) ? acc : [...acc, i], []);

console.log(result);