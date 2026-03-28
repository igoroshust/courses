let string = '1 22 333 4444 22 5555 1';
const result = string.split(' ').filter(i => i.length <= 3).join(' ')

console.log(
    result
);