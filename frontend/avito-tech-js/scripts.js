const str = 'abcde';

const result = str.replace(/(.)(.)/g, (match, p1, p2) => p1.toUpperCase() + p2)

console.log(result);