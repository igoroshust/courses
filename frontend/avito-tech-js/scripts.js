const str = 'aaa bbb ccc eee fff';

const result = str.replace(
  /\b([a-z])([a-z]+)(?=\s+\w+\b)/g,
  (match, first, rest) => first.toUpperCase() + rest
);

console.log('result :>> ', result);