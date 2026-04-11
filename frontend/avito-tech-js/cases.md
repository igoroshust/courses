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

Мой кастомный вариант
```javascript
const numbers = [1, 2, 3, 3, 4, 5];

const addRandomNumbers = (arr, count) => {
    const currentLength = arr.length;
    while (currentLength + count > arr.length) {
        arr.push(Math.floor(Math.random() * 100))
    }
};

addRandomNumbers(numbers, 5)

console.log(numbers);
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

### Вернуть массив индексов '0'
Моё решение
```javascript
const string = '023m0df0dfg0';
const result = string.split("").reduce((acc, item, index) => item === '0' ? acc.concat(index) : acc, []);
```

### Удалить каждый третий символ в строке
```javascript
let str = 'abcdefg';
let formattedString = '';

for (let i = 0; i < str.length; i += 3) formattedString += str.slice(i, i + 2);

console.log('formattedString :>> ', formattedString);
```

### Поделить сумму чётных элементов на нечётные
`reduce`
```javascript
const arr = [1, 2, 3, 4, 5, 6];

const strangeFunction = array => {
    const { evenSum, oddSum } = array.reduce((acc, num) => {
        if (num % 2) === 0 {
            acc.evenSum += num;
        } else {
            acc.oddSum += num;
        }
        return acc;
    }, { evenSum: 0, oddSum: 0 });

    if (oddSum === 0) throw new Error('Деление на ноль!');
    return evenSum / oddSum;
}

console.log(strangeFunction(arr)); // 6/15 = 0.4 (правильно!)
```

Тернарный оператор в reduce (компактно)
```javascript
const arr = [1, 2, 3, 4, 5, 6];

const strangeFunction = array => {
    const { evenSum, oddSum } = array.reduce((acc, num) => ({
        evenSum: acc.evenSum + (num % 2 === 0 ? num : 0),
        oddSum: acc.oddSum + (num % 2 === 0 ? num : 0),
    }, { evenSum: 0, oddSum: 0 });

    return oddSum ? evenSum / oddSum : Infinity;
```

Функциональный стиль с filter/map
```javascript
const strangeFunction = array => {
    const evenSum = array.filter(n => n % 2 === 0).reduce((a, b) => a + b, 0);
    const oddSum = array.filter(n => n % 2 !== 0).reduce((a, b) => a + b, 0);
    
    return oddSum ? evenSum / oddSum : Infinity;
};
```


Моё решение
```javascript
const arr = [1, 2, 3, 4, 5, 6];

const strangeFunction = array => {
    let evenNumbers=0;
    let oddNumbers=0;

    array.forEach(item => item % 2 === 0 ? evenNumbers += item : oddNumbers += item);
    return parseFloat((evenNumbers / oddNumbers).toFixed(2));
}

const result = strangeFunction(arr);
console.log(typeof result);
```

### Дана некоторая строка с буквами и цифрами. Получите массив позиций всех цифр из этой строки.
`for...of` (самое быстрое, 12ms)
```javascript
const str = 'abc23sd543lcsdf32';
const result = [];
for (let i = 0; i < str.length; i++) {
    if (/\d/.test(str[i])) result.push(i)
}
```

`reduce + push`
```javascript
const str = 'abc23sd543lcsdf32';

const result = str.split('').reduce((acc, item, index) => Number.isInteger(+item) ? (acc.push(index), acc) : acc, []); // запятая-оператор возвращает последнее значение

console.log(result);
```

`matchAll + flatMap`
```javascript
const str = 'abc23sd543lcsdf32';

const result = [...str.matchAll(/\d/g)].flatMap(match => match.index);

console.log(result);
```

`Array.from + условие`
```javascript
const str = 'abc23sd543lcsdf32';

const result = Array.from(str, (_, i) => i).filter(i => /\d/.test(str[i]));

console.log(result);
```

`replace + callback`
```javascript
const str = 'abc23sd543lcsdf32';

str.replace(/\d/g, (match, offset) => {
    result.push(offset);
    return match;
});
```

Моё решение
```javascript
const str = 'abc23sd543lcsdf32';

const result = str.split("").reduce((acc, item, index) => Number.isInteger(+item) ? acc.concat(index): acc, []);
```

### Развернуть элементы внутри массива
Функциональный стиль (самый производительный)
```javascript
const arr = [123, 456, 789];
const result = arr.map(num => String(num).split('').reverse().join(''))
```

map (на втором месте по производительности)
```javascript
const arr = [123, 456, 789];
const result = arr.map(n => +[...String(n)].reverse().join(''));
```

С математическим реверсом (без строк)
```javascript
const arr = [123, 456, 789];

const reverseNum = num => {
    let reversed = 0;
    while (num > 0) {
        reversed = reversed * 10 + num % 10; // iter-1: 3, iter-2: 32, iter-3: 321, iter-4: 6, iter-5: 65, iter-6: 654,
        console.log('reversed :>> ', reversed);
        num = Math.floor(num / 10); // iter-1: 12, iter-2: 1, iter-3: 0, iter-4: 45, iter-5: 4, iter-6: 0
        console.log('num :>> ', num);
    }
    return reversed;
};

const result = arr.map(reverseNum);

console.log('result :>> ', result);
```

Моё решение
```javascript
const arr = [123, 456, 789];
const result = arr.reduce((acc, item) => (acc.push(+String(item).split("").reverse().join("")), acc), []);
```

Array.from
```javascript
const arr = [123, 456, 789];
const result = arr.map(num => Array.from(String(num), Number)
    .reverse()
    .join('')
);
```

С отрицательными числами
```javascript
const arr = [123, 456, 789];

const reverseNum = num => {
    const sign = Math.sign(num) // возвращает знак числа (1 или -1)
    const absNum = Math.abs(num); // число без знака
    const reversed = String(absNum) // "321"
        .split('').reverse().join('');
    return sign * Number(reversed); // -321 или 321
};

console.log(reverseNum(123));  // 321
console.log(reverseNum(-123)); // -321
```








### Отделить тройки значений в строковом ряду
Лучшее решение
```javascript
const str = "123456782346524132"; // 1 234 567

const formatSpecial = (str) => 
    str.length ? [str[0], ...str.slice(1).match(/.{1,3}/g)].join(' ').trim() : '';

console.log(formatSpecial("123456789"));  // "1 234 456 789" ✅
```

Моё решение
```javascript
const str = "123456782346524132"; // 1 234 567

let resultString = [];

for (let i = 0; i < str.length; i += 3) {
    resultString += str[i] + " " + str.slice(i+1, i + 3);
  console.log(resultString);
}

console.log("resultString :>> ", resultString);
```

Исправленное моё решение
```javascript
const str = "123456789";
let resultString = str[0];  // первый символ отдельно

for (let i = 1; i < str.length; i += 3) {
    if (i > 0) resultString += " ";  // пробел только между группами
    resultString += str.slice(i, i + 3);
}

console.log(resultString);  // "1 234 456 789" ✅
```

match + join
```javascript
const str = "123456789";
const result = [str[0], ...str.slice(1).match(/.{1,3}/g)].join(' ').trim();
console.log(result);  // "1 234 456 789" ✅
```

Регулярное выражение
```javascript
const str = "123456789";
const result = str.replace(/^(.)(.{3})*(.*)$/, '$1 $2$3').trim();
console.log(result);  // "1 234 456 789" ✅
```

Однострочный regex
```javascript
const formatSpecial = (str) => str.replace(/(.)(.{3})*/g, (m, first) => first + (m.slice(1).match(/.{3}/g)?.join(' ') || ''));
```

Универсальная функция
```javascript
const str = "123456782346524132"; // 1 234 567

const formatSpecial = (str) => {
    if (str.length === 0) return '';
    
    const first = str[0];
    const rest = str.slice(1).match(/.{1,3}/g) || [];
    return [first, ...rest].join(' ').trim();
};

console.log(formatSpecial("123456789"));  // "1 234 456 789"
console.log(formatSpecial("1234567"));    // "1 234 567"
console.log(formatSpecial("12345"));      // "1 234 5"
console.log(formatSpecial("123"));        // "1 23"
console.log(formatSpecial("12"));         // "1 2"
console.log(formatSpecial("1"));          // "1"
```


### Изменить регистр каждой буквы строки на противоположный

Моё решение
```javascript
const str = 'AbCdE';

const reverseRegister = str.split("").reduce((acc, item) => item === item.toUpperCase() ? acc + item.toLowerCase() : acc + item.toUpperCase(), '');
```

map
```javascript
const reverseRegister = str
  .split('')
  .map(char => 
    char === char.toUpperCase() 
      ? char.toLowerCase() 
      : char.toUpperCase()
  )
  .join('');

console.log(reverseRegister); // 'aBcDe'
```

Регулярное выражение
```javascript
const reverseRegister = str
    .replace(/[a-z]/g, c => c.toUpperCase())
    .replace(/[A-Z]/g, c => c.toLowerCase());

console.log(reverseRegister);
```


### Слепить пары чисел массива вместе
forEach
```javascript
const numbers = [1, 2, 3, 4, 5, 6];
const result = [];

numbers.forEach((item, index) => {
  if (index % 2 === 0) {
    result.push(String(item));
  } else {
    result[result.length - 1] += String(item);
  }
});

console.log('result :>> ', result); // ['12', '34', '56']
```

Моё решение
```javascript
const numbers = [1, 2, 3, 4, 5, 6];

const result = numbers.reduce((acc, item, index) => index % 2 === 0 ? (acc.push(String(item)), acc) : (acc[acc.length-1] += String(item), acc), []).map(Number);

console.log('result :>> ', result);
```

Через for
```javascript
const numbers = [1, 2, 3, 4, 5, 6];

const result = [];
for (let i = 0; i < numbers.length; i += 2) {
  const pair = String(numbers[i]) + (numbers[i + 1] !== undefined ? String(numbers[i + 1]) : '');
  result.push(pair);
}

console.log('result :>> ', result); // ['12', '34', '56']
```


## Заменить в строке первую букву каждого второго слова на заглавную

Моё решение с map
```javascript
const str = 'aaa bbb ccc eee fff';

const result = str.split(" ");

const transformRegister = string => result.reduce((acc, item, index) => index % 2 === 0 ? (acc.push(item),acc) : (acc.push(item[0].toUpperCase() + item.slice(1)), acc),[]).join(" ")

console.log(
    transformRegister(str)
);

// map эффективнее, поскольку создаёт новый массив за один проход, зная его длину (равна длине исходного массива)
// + внутренняя реализация оптимизирована специально для преобразования элементов
// + меньше операций на итерацию
```

Моё решение c reduce
```javascript
const str = 'aaa bbb ccc eee fff';

const result = str.split(" ");

const transformRegister = string => result.reduce((acc, item, index) => index % 2 === 0 ? (acc.push(item),acc) : (acc.push(item[0].toUpperCase() + item.slice(1)), acc),[]).join(" ")

console.log(
    transformRegister(str)
);
```

for...of с индексом
```javascript
const str = 'aaa bbb ccc eee fff';

const words = str.split(' ');
const result = [];

for (let [i, word] of words.entries()) {
    result.push(i % 2 === 0 ? word : word[0].toUpperCase() + word.slice(1));
}

console.log(result.join(' '));
```

## Перевести в верхний регистр элементы списка с количеством букв меньше или равно 3
С обработкой edge-кейсов (производственный код)
```javascript
const str = 'a bc def ghij';

const upperCaseShortWords = string => {
  return string
    .trim()
    .split(/\s+/)
    .map(word => word.length <= 3 ? word.toUpperCase() : word)
    .filter(Boolean) // убираем пустые строки
    .join(' ');
}

console.log('upperCaseShortWords :>> ', upperCaseShortWords(str));

// \s - любой пробельный символ (пробел, таб, перенос строки \n, \r)
// + - 1 или более подряд
```


Моё решение
```javascript
const str = 'a bc def ghij';

const result = str
  .split(' ')
  .map(item => item.length <= 3 ? item.toUpperCase() : item)
  .join(' ');

console.log('result :>> ', result);
```

Регулярные выражения
```javascript
const str = 'a bc def ghij  i j k lmno';
const result = str.replace(/\b\w{1,3}\b/g, match => match.toUpperCase());
console.log(result); // "A BC DEF GHIJ  I J K LMNO"

//    ├─ \b           - граница слова (начало/конец слова)
//    ├─ \w{1,3}      - 1-3 буквы/цифры/подчёркивания
//    ├─ \b           - граница слова
//    └─ g            - глобальный флаг (все совпадения)
```


## Отсортировать массив объектов по свойству age
Мутабельный вариант
```javascript
/* Напишите функцию, которая принимает массив объектов и сортирует его по возрастанию значения свойства “age” */

const objectsArr = [
  {
    name: 'Igor',
    age: 29,
  },
  {
    name: 'Egor',
    age: 19,
  },
  {
    name: 'Gregor',
    age: 39,
  },
];

function sortByAge(arr) {
    return arr.sort((a, b) => a.age - b.age);
}

console.log('sortByAge(objectsArr) :>> ', sortByAge(objectsArr));
```

Иммутабельный вариант
```javascript
function sortByAge(arr) {
    return [...arr].sort((a, b) => a.age - b.age); // Новый массив
}
```

## Определить регистр символа
```javascript
let char = 'j';

const defineCharRegister = char => 
    !/[a-zA-Z]/.test(char) ? 'not a letter' :
    char === char.toUpperCase() ? 'Upper' : 'lower';

console.log(
    defineCharRegister(char)
);
```

## Оставить только чётные числа
for...of (самый быстрый и читаемый)
```javascript
const getEvenDigits = num => {
    let result = '';
    for(const digit of String(Math.abs(num))) {
        if(digit % 2 === 0) result += digit;
    }
    return result;
};

// for...of: 67ms ⚡ Самый быстрый + читаемый!
```

Моё решение
```javascript
const result = num => 
    String(Math.abs(num))  // ✅ abs() + String()
    .split('')
    .filter(i => i % 2 === 0)
    .join('');

// Тесты
console.log(result(123789));  // "24"
console.log(result(-123789)); // "24"
console.log(result(13579));   // ""
```

## Проверить, что в строке не более 2 символов в верхнем регистре
`match` - Самый производительный вариант
```javascript
const isCheck = str => (str.match(/[A-Z]/g) || []).length >= 2;
```

`for...of` (читаемость + быстрота)
```javascript
const isCheck = str => {
    let count = 0;
    for (const char of str) {
        if (char === char.toUpperCase()) {
            if (++count >= 2) return true;
        }
    }
    return false;
}
```

Современный способ
```javascript
const isCheck = str => Array.from(str, c => c.toUpperCase()).filter(
    (c, i) => c === str[i]
).length >= 2;
```

One-liner c reduce
```javascript
const isCheck = str => [...str].reduce((count, char) => 
    char === char.toUpperCase() ? count + 1 : count, 0
) >= 2;
```

Моё решение 
```javascript
let string = 'saofjJD';

const isCheck = string => {
    let count = 0;
    let i = 0;
    
    while (i < string.length) {
        if (string[i] === string[i].toUpperCase()) count++;
        i++;
        if (count >= 2) return true;
    }
    return false;
}

console.log(
    isCheck(string)
);
```

### Удалите из строки все подстроки, в которых количество символов больше трех

Моё решение
```javascript
let string = '1 22 333 4444 22 5555 1';
const result = string.split(' ').filter(i => i.length <= 3).join(' ')

console.log(
    result
);
```

Цикл for + массив 
```javascript
let string = '1 22 333 4444 22 5555 1';
const words = string.split(' ');
const result = [];

for (let word of words) {
  if (word.length <= 3) {
    result.push(word);
  }
}
console.log(result.join(' ')); // "1 22 333 22 1"
```

Регулярное выражение + нормализация пробелов
```javascript
let string = '1 22 333 4444 22 5555 1';
const result = string
  .replace(/\b\w{4,}\b/g, '')
  .replace(/\s+/g, ' ')
  .trim();

console.log(result); // "1 22 333 22 1"
```

regex + match
```javascript
let string = '1 22 333 4444 22 5555 1';
const result = string.match(/\b\w{1,3}\b/g)?.join(' ') || '';

console.log(result); // "1 22 333 22 1"
```


## Даны два массива. Слейте их в один следующим образом: [1, 2, 'a', 'b', 'c', 3]

slice + spread (самый производительный)
```javascript
let arr1 = [1, 2, 3];
let arr2 = ['a', 'b', 'c'];

const mergeArrays = (arr1, arr2, insertIndex = 2) => [
    ...arr1.slice(0, insertIndex), 
    ...arr2, 
    ...arr1.slice(insertIndex)
];

const result = mergeArrays(arr1, arr2); // [1, 2, 'a', 'b', 'c', 3]
```

splice
```javascript
let arr1 = [1, 2, 3];
let arr2 = ['a', 'b', 'c'];

arr1.splice(2, 0, ...arr2); // [ 1, 2, 'a', 'b', 'c', 3 ]
```

Моё решение
```javascript
let arr1 = [1, 2, 3];
let arr2 = ['a', 'b', 'c'];

const strangeFunction = (arr1, arr2) => {
    let combined = [...arr1, ...arr2];

    const findElement = combined.splice(2, 1);
    combined.push(...findElement)

    return combined
}

const result = strangeFunction(arr1, arr2);
```

slice + concat
```javascript
let arr1 = [1, 2, 3];
let arr2 = ['a', 'b', 'c'];

const result = [...arr1.slice(0, 2), ...arr2, ...arr1.slice(2)];
// [1, 2, 'a', 'b', 'c', 3]
```


reduce
```javascript
let arr1 = [1, 2, 3];
let arr2 = ['a', 'b', 'c'];

const result = arr1.reduce((acc, curr, i) => {
    if (i === 2) acc.push(...arr2);
    acc.push(curr);
    return acc;
}, []);
// [1, 2, 'a', 'b', 'c', 3]
```

map + условие
```javascript
let arr1 = [1, 2, 3];
let arr2 = ['a', 'b', 'c'];

const result = arr1.map((item, i) => 
    i === 2 ? [...arr2, item] : item
).flat();
// [1, 2, 'a', 'b', 'c', 3]
```


## Найти сумму пар элементов числа 123456 (12 + 34 + 56)
Оптимальный по времени и дополнительной памяти (O(n) время, O(1) доп. память (кроме строки)) -  ~0.05ms
```javascript
let number = 123456; 

const sumDigitPairs = (num) => {
    const str = String(Math.abs(num));
    let sum = 0;

    for (let i = 0; i < str.length; i += 2) {
        const pair = +str.slice(i, i + 2) || 0;
        sum += pair;
    }

    return sum;
}


const result = sumDigitPairs(number);

console.log(result);
```

Математический способ (Работает с очень большими числами, минимум памяти) - ~0.03ms
```javascript
let number = 123456; 

const sumDigitPairs = (num) => {
    let sum = 0;
    let reminder;

    while (num > 0) {
        reminder = num % 100; // 56
        sum += reminder;
        num = Math.floor(num / 100); // 1234
    }
    return sum;
}

const result = sumDigitPairs(number);

console.log(result);
```


Моё решение -  ~0.1ms
```javascript
let number = 123456; 

const pairSum = num => {
    let sum = 0;
    let stringNumber = String(number);

    for (let i = 0; i < stringNumber.length; i += 2) {
        sum += +stringNumber.slice(i, i + 2);
    }

    return sum;
}

const result = pairSum(number);

console.log(result);
```

Функциональный стиль
```javascript
let number = 123456; 

const sumDigitPairs = (num) => 
    String(num)
        .match(/.{1,2}/g) // ['12', '34', '56']
        ?.reduce((acc, pair) => acc + +pair, 0) ?? 0;


const result = sumDigitPairs(number);

console.log(result);
```


## Вывести элементы массива в обратном порядке
Классический цикл for
```javascript
let arr = [1, 2, 3, 4, 5];

const reverseArray = array => {
    const resultArray = [];
    for (let i = array.length - 1; i >= 0; i--) resultArray.push(array[i])
    return resultArray;
}

console.log(reverseArray(arr)); // [5, 4, 3, 2, 1]
```

Встроенный метод reverse
```javascript
let arr = [1, 2, 3, 4, 5];

const reverseArray = array => [...array].reverse() // [...array] создаёт копию
console.log(reverseArray(arr)); // [5, 4, 3, 2, 1]
```

Однострочник
```javascript
let arr = [1, 2, 3, 4, 5];

console.log(arr.toReversed());
```

slice + reverse
```javascript
let arr = [1, 2, 3, 4, 5];

const reverseArray = array => array.slice().reverse()
console.log(reverseArray(arr)); // [5, 4, 3, 2, 1]
```

unshift
```javascript
let arr = [1, 2, 3, 4, 5];

const reverseArray = array => {
    const resultArray = [];
    for (let i = 0; i < array.length; i++) result.unshift(array[i]);
    return resultArray;
}
```



Моё решение
```javascript
let arr = [1, 2, 3, 4, 5];

const reverseArray = array => {
    const resultArray = []

    for (let i = -1; i >= -arr.length; i--) {
    resultArray.push(array.at(i))
    } 
    
    return resultArray;
}

console.log(reverseArray(arr));
```


## Проверить, что в строке не более 3 букв

Регулярное выражение
```javascript
let str = 'ad33424234e'

const hasNoMoreThanThreeLetters = string => (/[a-zA-Z]/g).test(string) ? (string.match(/[a-zA-Z]/g) || []).length <= 3 : true;

console.log(hasNoMoreThanThreeLetters('ad33424234e')); // false (4 буквы)
console.log(hasNoMoreThanThreeLetters('12345')); // true
console.log(hasNoMoreThanThreeLetters('abc123')); // true (3 буквы)
```

match() + length
```javascript
const hasNoMoreThanThreeLetters = string => (string.match(/[a-zA-Z]/gi) || []).length <= 3;
```

Поддержка кириллицы
```javascript
let str = 'aDDDDd33424234e'

const hasNoMoreThanThreeLetters = str => 
    (str.match(/[a-zA-Zа-яё]/gi) || []).length <= 3;

```

filter
```javascript
let str = 'aDDDDd33424234e'

const hasNoMoreThanThreeLetters = string => string.split('').filter(char => /[a-zA-Z]/.test(char)).length <= 3;

console.log(hasNoMoreThanThreeLetters('DDD33424234')); // false (4 буквы)
console.log(hasNoMoreThanThreeLetters('12345')); // true
console.log(hasNoMoreThanThreeLetters('abc123')); // true (3 буквы)
```


Моё решение
```javascript
let str = 'ad33424234e'

const isLteThreeWords = string => {
    let count = 0;
    for (let i = 0; i < str.length; i++) {
        if (string[i].charCodeAt() >= 65 && string[i].charCodeAt() <= 122) count++;
        if (count === 3) return true;
    }
    return false;
};

const result = isLteThreeWords(str);
console.log('result :>> ', result);

// A-Я 1040-1071
// а-я 1072-1103

// A-z 65-122

// console.log(Math.floor(Math.random(65, 122) * 10));
```

Моё решение через reduce
```javascript
const result = str.split('').reduce((acc, item) => {
    if (item.charCodeAt() >= 65 && item.charCodeAt() <= 122) {
        acc += item;
        if (acc.length >= 3) return true
    } 
    return false;
}, '');

console.log('result :>> ', result);
```


## Функция-генератор случайных чисел (включая границы)
```javascript
const randomIntInclusive = (min, max) => 
    Math.floor(Math.random() * (max - min + 1)) + min;

console.log(randomIntInclusive(65, 122)); // 65-122
console.log(randomIntInclusive(1, 6));    // 1-6 (кости)
```

## Функции-утилиты для генерации случайных данных разных типов

```javascript
// Универсальная функция
const random = {
    int: (min, max) => Math.floor(Math.random() * (max - min + 1)) + min,
    float: (min, max) => Math.random() * (max - min) + min,
    choice: arr => arr[random.int(0, arr.length - 1)],
    char: (min, max) => String.fromCharCode(random.int(min, max))
};

// Использование
console.log(random.int(1, 100));     // 42
console.log(random.float(1.5, 2.5)); // 2.123
console.log(random.choice(['a','b','c'])); // 'b'
console.log(random.char(65, 90));    // 'K'
```

## Вернуть первую чётную цифру с конца числа
find / findLast
```javascript
let number = 23923123;

const lastEvenNumber = +String(number).split('').reverse().find(i => i % 2 === 0); // Можно использовать findLast

console.log(lastEvenNumber);
```

Через while
```javascript
let number = 23923123;

const lastEvenNumber = num => {
    let str = String(num);
    let i = str.length;
    while (i--) {
        if (+str[i] % 2 === 0) return str[i];
    }
};
console.log(lastEvenNumber(number));
```

reduceRight
```javascript
const lastEvenNumber = num => 
    String(num)
    .split('')
    .reduceRight((acc, char) => acc || (+char % 2 === 0 ? char : null), null);
```


for...of 
```javascript
let number = 23923123;

const lastEvenNumber = num => {
    for (const char of String(num).split('').reverse()) {
        if (+char % 2 === 0) return char;
    }
};

console.log(lastEvenNumber(number));
```

Решение через цикл
```javascript
let number = 23923123;

const getLastEvenNumber = (num) => {
  let stringNum = String(num);

  for (let i = stringNum.length - 1; i >= 0; i--) {
    const digit = +stringNum[i];
    if (!isNaN(digit) && digit % 2 === 0) return digit;
  }
  return null;
};

console.log(getLastEvenNumber(number));
```


Моё решение
```javascript
let number = 23923123;

const getLastEvenNumber = num => {
    let stringNum = String(num);

    for (let i = stringNum.length - 1; i >= 0; i--) {
    if (+stringNum[i] % 2 === 0) return +stringNum[i];
}};

console.log(
    getLastEvenNumber(number)
);
```


match + regexp
```javascript
const lastEvenNumber = num => 
    String(num).match(/[02468](?=[^02468]*$)/)?.[0];
```

String.prototype.matchAll
```javascript
const lastEvenNumber = num => {
    const match = String(num).matchAll(/[02468]/g);
    return [...match].pop()?.[0];
};
```


Функция-генератор
```javascript
function* evenDigits(str) {
    for (let i = str.length - 1; i >= 0; i--) {
        if (+str[i] % 2 === 0) yield str[i];
    }
}
const lastEvenNumber = num => evenDigits(String(num)).next().value;
```