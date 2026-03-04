### Дано число 12345, получите массив цифр этого числа
```javascript
const num = '12345';
const arrayIntegers = String(num).split("").map(Number);

console.log(
    arrayIntegers
);
```


### Округлить дроби до одного знака в дробной части
```javascript
let arr = [1.456, 2.125, 3.32, 4.1, 5.34];

// Округление в большую сторону
let formattedArr = arr.map(item => Math.round(item * 10) / 10); // [1.5, 2.1, 3.3, 4.1, 5.3]

// toFixed() - возвращает строку, а не число (можно использовать + вместо parseFloat)
let formattedArr = arr.map(item => parseFloat(item.toFixed(1))); // [1.5, 2.1, 3.3, 4.1, 5.3]

// Без округления
let formattedArr = arr.map(item => Math.floor(item * 10) / 10); // [1.4, 2.1, 3.3, 4.1, 5.3]
```