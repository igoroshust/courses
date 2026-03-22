const numbers = [1, 2, 3, 4, 5, 6];

const result = numbers.reduce((acc, item, index) => index % 2 === 0 ? (acc.push(String(item)), acc) : (acc[acc.length-1] += String(item), acc), []).map(Number);

console.log('result :>> ', result);
