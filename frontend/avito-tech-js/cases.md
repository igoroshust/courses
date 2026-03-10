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