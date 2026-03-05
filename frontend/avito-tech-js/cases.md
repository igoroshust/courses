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

### Дан массив с числами. Увеличьте каждое число из массива на 10 процентов.
```javascript
const nums = [12, 32, 25, 22]

const test = nums.map(item => (item * 1.1).toFixed(1))
```

### Добавить в массив 5 случайных чисел 
```javascript
let arr = [];

// Math.floor (целое от 0 до 99)
for (let i = 0; i < 5; i++) {
    arr.push(Math.floor(Math.random() * 100) + 1); // +1 добавляем до 100
}

// Array.from() + map()
const arr = Array.from({ length: 5 }, () => Math.floor(Math.random() * 100) + 1)

// Array + fill + map
const arr = Array(5).fill().map(() => Math.floor(Math.random() * 100) + 1);
// Array создаёт массив из 5 элементов, fill заполняет его значениями (undefined), map заменяет каждый элемент на случайное число.

// с циклом while
let arr = [], count = 5;
while (count--) arr.push(Math.floor(Math.random() * 100) + 1);
```

### Выведите все символы числа с конца
```javascript
let num = 12345;

// Моё решение
for (let i = String(num).length - 1; i >= 0; i--) {
    console.log(String(num)[i])
}

// Через split() + reverse() + forEach (выводит каждый элемент)
String(num).split('').reverse().forEach(digit => console.log(digit))

// Математический вариант
while (num > 0) {
    console.log(num % 10); // Остаток от деления на 10 - последняя цифра
    num = Math.floor(num / 10);
}

// Через reduceRight()
String(num).split('').reduceRight((_, digit) => {
    console.log(digit);
    return null;
}, null);
```

### Преобразовать элементы массива в строку в обратном порядке
```javascript
const letters = ['a', 'b', 'c', 'd'];
const result = letters.reduceRight((acc, item) => acc + item, '');
console.log(result);
```