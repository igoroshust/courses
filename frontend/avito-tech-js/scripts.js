const number = 13239545;
const str = String(number);
let count = 0;

for (const char of str) {
    if (!isNaN(char) && Number(char) % 2 === 0) {
        count++;
    }
}

console.log(count);