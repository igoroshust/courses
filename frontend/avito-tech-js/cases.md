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


### Вывести по 2 элемента массива
```javascript
let arr = [1, 2, 3, 4, 5, 6];

// Моё решение
let arrBit = [];
for (let i = 0; i < arr.length; i++) {
    arrBit.push(arr[i])
    if (arrBit.length === 2) {
        console.log(arrBit);
        arrBit = [];
    }
}

// slice
for (let i = 0; i < arr.length; i += 2) {
    console.log(arr.slice(i, i + 2));
}
```


### Удалить элементы из массива
```javascript
let arr = ["wads", "asda", 213, null,  "asda",  "asda", 444, 22];

// Моё решение
arr = arr.filter(item => item !== "asda")

// for + splice (цикл идёт с конца, чтобы избежать проблем с изменением индексов при удалении элементов, не пропустить элементы из-за сдвига индексов)
for (let i = arr.length - 1; i >= 0; i--) {
    if (arr[i] === "asda") {
        arr.splice(i, 1);
    }
}

// while + indexOf()
let index;

while ((index = arr.indexOf("asda")) !== -1) {
    arr.splice(index, 1);
}
```

### Посчитать сумму половины элементов массива
```javascript
let arr = [1, 2, 3, 4, 5, 6];
let mid = Math.floor(arr.length / 2); // Чёткое определение первой половины (для нечетных элементов округление вниз), ceil - округление вверх
let arrBitSum = arr.slice(0, mid).reduce((acc, item) => acc + item, 0);


// Через for
let sum = 0;
let mid = Math.floor(arr.length / 2);

for (let i = 0; i < mid; i++) {
    sum += arr[i];
}
```

### Посчитать количество отрицательных чисел
```javascript
let arr = [1, 2, -3, 4, 5, 6, -1, -2, -3];
let result = arr.reduce((acc, item) => item < 0 ? acc += 1 : acc, 0)
```

### Поделить значения первой части массива на значения второй
Моё решение
```javascript
function divideArrayChunks(arr) {
    let firstChunkSum = arr.slice(0, Math.floor(arr.length / 2)).reduce((acc, item) => acc + item, 0);
    let secondChunkSum = arr.slice(Math.floor(arr.length / 2)).reduce((acc, item) => acc + item, 0);

    return firstChunkSum / secondChunkSum;
};


const result = divideArrayChunks([1, 2, 3, 4, 5, 6]);

console.log(
    result
);
```

С вычислением середины
```javascript
const divideArrayChunks = arr => {
    const mid = arr.length >> 1;
    const sum1 = arr.slice(0, mid).reduce((a, b) => a + b, 0);
    const sum2 = arr.slice(mid).reduce((a, b) => a + b, 0);
    return sum2 === 0 ? 0 : sum1 / sum2; // Защита от деления на 0
};
```

В одну строку
```javascript
const divideArrayChunks = arr => arr.slice(0, arr.length >> 1).reduce((a, b) => a + b, 0) / arr.slice(arr.length >> 1).reduce((a, b) => a + b, 0);
```

### Удалить предпоследний символ строки
```javascript
const removeSecondLast = (str) => str.slice(0, 2) + str.slice(-1)
```

### Сравнить, начинается ли вторая строка с последнего символа первой строки
```javascript
const isSampleWords = (firstString, secondString) => 
  firstString.at(-1) === secondString.at(0);
```

### Найти позицию третьего нуля в строке
```javascript
const thirdZeroIndex = str => {
    let index = -1;
    for (let i = 0; i < 3; i++) {
        index = str.indexOf('0', index + 1); // Второй параметр - с какого элемента начинаем поиск
        if (index === -1) return -1
    }
    return index;
}
```

Через split + filter
```javascript
const thirdZeroIndex = str => {
    const zeros = str.split('').map((char, i) => char === '0' ? i : -1).filter(i => i !== -1);
    return zeros[2] ?? -1;
}
```

### Найти сумму чисел, разделённых запятой
```javascript
const string = '12,34,56';

// Моё решение
const result = string.split(",").reduce((acc, item) => acc+ +item, 0);
```

### Преобразовать дату в объект
```javascript
const date = '2025-12-31';

/* Деструктуризация */
const [year, month, day] = date.split('-'); // Создаём 3 переменные `year = '2025'` и тд
const obj = { year, month, day }; // Объект с сокращённым синтоксисом
// js автоматически понимает, что эти две строки есть запись `const obj = { year: year, month: month, day: day }`

/* Моё решение */
const arrDate = date.split('-');
const params = ['year', 'month', 'day']
const obj = new Object;
for (let i = 0; i < params.length; i++) obj[`${params[i]}`] = arrDate[i];
```


### Дана некоторая строка с буквами и цифрами. Получите позицию первой цифры в этой строке.
search + регулярное выражение
```javascript
const getNumberIndex = str => str.search(/\d/);
```

findIndex() + test()
```javascript
const getNumberIndex = str => 
    [...str].findIndex(char => /\d/.test(char));
```

match() + регулярное выражение
```javascript
const getNumberIndex = str => {
    const match = str.match(/\d/);
    return match ? str.indexOf(match[0]) : -1;
}
```



Моё решение
```javascript
const getNumberIndex = str => {
  for (let i = 0; i < str.length; i++) {
    if (!Number.isNaN(+str[i])) return i;
  }
  return -1; // явный возврат при отсутствии цифры
};

const result = getNumberIndex('a2bcde2edf23ws');
console.log(result);
```


### Дан объект с ключами и значениями. Запишите в первый массив ключи объекта, а во второй - значения.
Использование `Object.keys()` + `Object.values()`
```javascript
const obj = {
    name: 'Igor',
    surname: 'Tvar',
    a: 1,
    b: 2,
    c: 3,
    d: 4,
};

const keys = Object.keys(obj);
const values = Object.values(obj);
```

Использование `Object.entries()` + `reduce`
```javascript
const { keys, values } = Object.entries(obj).reduce(
    (acc, [key, value]) => {
        acc.keys.push(key);
        acc.values.push(value);
        return acc;
    },
    {keys: [], values: [] }
)
```

Используя map
```javascript
const keys = Object.keys(obj);
const values = keys.map(key => obj[key]);
```

Использование деструктуризации
```javascript
for (const [key, value] of Object.entries(obj)) {
    keys.push(key);
    values.push(value);
}
```


Моё решение
```javascript
const keys = [];
const values = [];

for (let entry of Object.entries(obj)) {
    keys.push(entry[0]);
    values.push(entry[1]);
}

console.log('keys :>> ', keys);
console.log('values :>> ', values);
```


### Дано число. Выведите в консоль количество четных цифр в этом числе.
Через `for...of`
```javascript
const number = 13239545;
const str = String(number);
let count = 0;

for (const char of str) {
    if (!isNaN(char) && Number(char) % 2 === 0) count++
}
```

Через `filter()` + `length` (лучший вариант)
```javascript
const number = 13239545;
const result = String(number)
    .match(/\d/g)
    .filter(digit => Number(digit) % 2 === 0)
    .length;

console.log(result);
```

Через `reduce` + `match`
```javascript
const number = 13239545;

const result = String(number)
    .match(/\d/g)
    .reduce((acc, digit) => acc + (Number(digit) % 2 === 0 ? 1 : 0), 0);
```

Математический способ
```javascript
const number = 13239545;
let n = Math.abs(number); // Убираем знак минус
let count = 0;

while (n > 0) {
    const digit = n % 10; // Получаем последнюю цифру
    if (digit % 2 === 0) count ++
    n = Math.floor(n / 10); // Убираем последнюю цифру
}
```


Моё решение
```javascript
const number = 13239545;
const result = String(number).split("").reduce((acc, item) => +item % 2 === 0 ? acc += 1 : acc, 0);

console.log(result);
```

Мой исправленный вариант
```javascript
const number = 13239545;
const result = String(number)
  .split("")
  .reduce((acc, item) => {
    const digit = Number(item);
    return !isNaN(digit) && digit % 2 === 0 ? acc + 1 : acc;
  }, 0);
```


### Разбить текст на строки
```javascript
const sentences = ["Hello world", "JavaScript is fun"];

const words = sentences.flatMap(sentence => sentence.split(" "));
console.log(words); // ["Hello", "world", "JavaScript", "is", "fun"]
```

### Перевестив верхний регистр нечётные буквы строки
reduce
```javascript
const str = 'abcde';
const arr = str.split("");

const result = arr.reduce((acc, item, index) => {
    return acc + (index % 2 === 0 ? item.toUpperCase() : item);
}, '');


console.log(result);
```

Моё решение
```javascript
const str = 'abcde';
const result = str.split("").map((item, index) => index % 2 === 0 ? item.toUpperCase() : item).join("");
```

forEach
```javascript
const str = 'abcde';
const arr = str.split("");

arr.forEach((item, index) => {
    if (index % 2 === 0) {
        arr[index] = item.toUpperCase()
    }
});

const result = arr.join("");
console.log(result);
```

Через регулярное выражение
```javascript
const result = str.replace(/(.)(.)/g, (match, p1, p2) => p1.toUpperCase() + p2)

/* 
. - любой символ (кроме переноса строки)
() - захватыващие группы (сохраняют найденные символы, чтобы использовать их позже)
Первый (.) захватывает первый символ пары
Вторая (.) захватывает второй символ пары
g - флаг global (глобальный) - говорит двигателю искать все совпадения в строке, а не только первое.
Для 'abcde' найдётся 'ab' и 'cd'.

match - вся найденная подстрока ('ab', например)
p1 - содержимое первой группы (первый символ, 'a')
p2 - содержимое второй группы (второй символ, 'b')

p1.toUpperCase() + p2 - берём первый символ пары, делаем его заглавным, и добавляем второй символ как есть.
*/
```


### Капитализация каждого слова в строке
Лучшее решение
```javascript
// Лучший вариант по читаемости и производительности
const capitalizeWords = (str) => 
  str.split(' ')
     .map(word => word.charAt(0).toUpperCase() + word.slice(1))
     .join(' ');

console.log(capitalizeWords('aaa bbb ccc')); // "Aaa Bbb Ccc"
```

Через `map()` + `join()`
```javascript
let string = 'aaa bbb ccc';
let result = string
    .split(' ')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
```

Моё решение
```javascript
let string = 'aaa bbb ccc';
let result = string.split(" ").reduce((acc, item) => acc + (item.charAt(0).toUpperCase() + item.slice(1) + ' '), '').trim();
```

Через replace
```javascript
let string = 'aaa bbb ccc';
let result = string.replace(/\b\w/g, l => l.toUpperCase());

// \b\w - границы слова + любая буква
```


Через forEach
```javascript
let string = 'aaa bbb ccc';
let words = string.split(' ');
let result = '';

words.forEach(word => {
    result += word.charAt(0).toUpperCase() + word.slice(1) + ' ';
});

result = result.trim();
```

Через for
```javascript
let string = 'aaa bbb ccc';
let words = string.split(' ');
let result = '';

for (let i = 0; i < words.length; i++) {
    result += words[i].charAt(0).toUpperCase() + words[i].slice(1);
    if (i < words.length - 1) result += ' ';
}
```
