// const numbers = [...Array(11).keys()].map(i => i + 10).forEach(num => console.log(num));

const numbers = Array.from({length: 11}).map((_, i) => i + 10);
numbers.forEach(num => console.log(num))