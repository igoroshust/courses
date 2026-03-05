const letters = ['a', 'b', 'c', 'd'];
const result = letters.reduceRight((acc, item) => acc + item, '');
console.log(result);