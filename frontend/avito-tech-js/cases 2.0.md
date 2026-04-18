## Заменить первый символ каждого слова
Функциональный вариант
```javascript
const replaceFirstLetter = str => 
  str.split(' ')
     .map(word => '!' + word.slice(1))
     .join(' ');
```


Моё решение
```javascript
let string = 'abcde abcde abcde';

const result = string.split(' ').reduce((acc, i) => `${acc + i.replaceAll(i[0], '!')} `, '').trimEnd();
```

Через map
```javascript
let string = "abcde abcde abcde";

const replaceFirstSymbol = (str, symbol = "!") => {
  const chunks = str.split(" ");
  return chunks.map(chunk => symbol + chunk.slice(1)).join(' ');
};

console.log(replaceFirstSymbol(string));
```


Через for...of
```javascript
let string = "abcde abcde abcde";

const replaceFirstSymbol = (str, symbol = "!") => {
  const chunks = str.split(" ");
  let result = "";
  
  for (let chunk of chunks) {
    result += symbol + chunk.slice(1) + " ";
  }
  
  return result.trimEnd();
};

console.log(replaceFirstSymbol(string)); // '!bcde !bcde !bcde'
```


## Проверить в массиве наличие двух одинаковых элементов подряд

Через for...of
```javascript
const arr = [1, 2, 3, 3, 4, 5];

function hasConsecutiveDuplicates(arr) {
  let prev = null;
  for (const current of arr) {
    if (prev !== null && prev === current) return true;
    prev = current
  }
  return false;
}

console.log(
  hasConsecutiveDuplicates(arr)
);
```

Через for
```javascript
function hasConsecutiveDuplicates(arr) {
    if (!arr || arr.length < 2) return false;
    
    for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i] === arr[i + 1]) return true;
    }
    return false;
}
```

Моё решение
```javascript
const arr = [1, 2, 3, 3, 4, 5];
const isEqual = arr.some((i, index) => arr[index] === arr[index+1]);

console.log(isEqual);
```

Рефакторинг моего решения
```javascript
const arr = [1, 2, 3, 3, 4, 5];

const hasConsecutiveDuplicates = arr => 
    arr?.length > 1 && arr.some((item, i) => item === arr[i + 1]);
console.log(hasConsecutiveDuplicates(arr));
```


## Проверить, что числа идут в порядке возрастания
Моё решение через for
```javascript
let number = 12345;

const tF = (num) => {
  let numberArray = String(num).split("");
  for (let i = 0; i < numberArray.length; i++) {
    if (numberArray[i] > numberArray[i + 1]) return false;
  }
  return true;
};
```

Через every
```javascript
let number = 12344;

const isIncreasing = (number) => {
  const digits = String(number).split('');
  return digits.slice(0, -1).every((digit, index) => 
    digit < digits[index + 1]
  );
};

console.log(isIncreasing(number));
```

Альтернатива через every
```javascript
let number = 123456;

const isIncreasing = (number) => {
  const digits = String(number).split('');
  return digits.every((d, i) => i === digits.length - 1 || d < digits[i+1])
};

console.log(isIncreasing(number));
```

Через reduce
```javascript
let number = 12345;

const isIncreasing = (num) => 
  String(num)
    .split('')
    .reduce((acc, d, i, arr) => acc && (i === arr.length - 1 || d <= arr[i + 1]), true);

console.log(isIncreasing(number));
```

Через sort 
```javascript
const isIncreasing = (num) => {
  const digits = String(num).split('');
  const sorted = [...digits].sort();
  return digits.join('') === sorted.join('');
};
```


## Удалить пустые элементы из массива

Финальное решение
```javascript
let arr = [1, '', 2, '', 3, '', '', 12, ' '];
const filtered = arr.filter(space => String(space).trim() !== '')

arr.length = 0; // Очищаем массив
arr.push(...filtered)

console.log(arr);
```

Мои варианты
```javascript
let arr = [1, '', 2, '', 3, '', '', 12, ' '];
const result = arr.filter(space => String(space).trim() !== '');
const removeBolean = arr.filter(Boolean); // неточно

// const strange = arr.join('').split('').map(Number); // под вопросом
```



## Отсортировать элементы в подмассиве
for...of (мутация, рекомендуемо при мутации)
```javascript
let arr = [
  [2, 1, 4, 3, 5],
  [3, 5, 2, 4, 1],
  [4, 3, 1, 5, 2],
];

for (const subArray of arr) subArray.sort((a, b) => b - a);

console.log(arr);
```

forEach + sort (рекомендуемо без мутации, лучше чем for + sort по читаемости)
```javascript
let arr = [
  [2, 1, 4, 3, 5],
  [3, 5, 2, 4, 1],
  [4, 3, 1, 5, 2],
];

const sortedArr = arr.map(subArray => [...subArray].sort((a, b) => b - a));

console.log(sortedArr);
```


map + sort
```javascript
let arr = [
  [2, 1, 4, 3, 5],
  [3, 5, 2, 4, 1],
  [4, 3, 1, 5, 2],
];

const sortedArr = arr.map(subArray => [...subArray].sort((a, b) => b - a));

console.log(sortedArr);
```

slice + map
```javascript
let arr = [
  [2, 1, 4, 3, 5],
  [3, 5, 2, 4, 1],
  [4, 3, 1, 5, 2],
];

const sortedArr = arr.map(subArray => subArray.slice().sort((a, b) => b - a));
```

Глубокое копирование + сортировка (костыль)
```javascript
let arr = [
  [2, 1, 4, 3, 5],
  [3, 5, 2, 4, 1],
  [4, 3, 1, 5, 2],
];

const sortedArr = JSON.parse(JSON.stringify(arr)).map(subArray => subArray.sort((a, b) => b - a));

console.log(sortedArr);
```


Моё решение (менее читаемо, но подходит для базовых случаев)
```javascript
let arr = [
	[2, 1, 4, 3, 5],
	[3, 5, 2, 4, 1],
	[4, 3, 1, 5, 2],
];

for (let i = 0; i < arr.length; i++){
    arr[i].sort((a, b) => b - a);
}

console.log(arr);
```


## Удалить элементы с конца второго массива до совпадения по длине с первым массивом
Универсальная функция
```javascript
let arr = [1, 2, 3];
let arr1 = [1, 2, 3, 4, 5];

function truncateToLength(array, targetLength) {
    const excess = array.length - targetLength;
    if (excess > 0) array.splice(-excess);
    return array;
}

console.log(
    truncateToLength(arr1, arr.length)
);
```


Через splice
```javascript
let arr = [1, 2, 3];
let arr1 = [1, 2, 3, 4, 5];

arr1.splice(-(arr1.length - arr.length))

console.log(arr1);
```

Через slice
```javascript
let arr = [1, 2, 3];
let arr1 = [1, 2, 3, 4, 5];

arr1 = arr1.slice(0, arr.length);

console.log(arr1);
```


Моё решение
```javascript
let arr = [1, 2, 3];
let arr1 = [1, 2, 3, 4, 5];

// While
while (arr1.length > arr.length) arr1.pop();

// For
for (let i = arr1.length - arr.length; i > 0; i--) {
    arr1.pop();
}

console.log(arr1);
```


## Вывести число в промежутке от 10 до 1000, если предпоследнее число чётное
Моё решение
```javascript
for (let i = 10; i <= 1000; i++) {
    if (String(i).at(-2) % 2 === 0) console.log(i);
}
```

## Вывести последовательность чисел
Через Array.from
```javascript
const numbers = Array.from({length: 11}, (_, i) => i + 10);
numbers.forEach(num => console.log(num));
```

Через spread
```javascript
const test = [...Array(11).keys()].map(i => i + 10).forEach(num => console.log(num));

console.log(test);
```


## Вернуть 2 при вводе 1, вернуть 1 при вводе 2
```javascript
// Через объекты
function example(n) {
    return {1: 2, 2: 1}[n];
}

// Через массивы
function example1(n) {
    return [2, 1][n-1]
}

// Через oneliner
function example2(n) {
    return 3 - n;
}
```


## Найти уникальные элементы в массиве
Моё решение
```javascript
const arr = [1, 2, 3, 3, 5];

const result = arr.reduce((acc, i) => acc.find(item => item === i) ? acc : (acc.push(i),acc), []);

console.log(result);
```

Set (Оптимальный O(n) - константное время)
```javascript
const arr = [1, 2, 3, 3, 5];

const result = [...new Set(arr)];

console.log(result);
```

Функциональный стиль без мутаций
```javascript
const arr = [1, 2, 3, 3, 5];

const result = arr.reduce((acc, i) => 
  acc.includes(i) ? acc : [...acc, i]), []);

console.log(result);
```


## Вывести количество нолей равному значению переменной

repeat (самый быстрый)
```javascript
let num = 5;
let result = '0'.repeat(num);

console.log(result);
```

Array.fill
```javascript
let num = 5;
let res = new Array(num).fill('0').join('');

console.log(res);
```

for
```javascript
let num = 5;
let res = '';

for (let i = 0; i < num; i++) res += '0'
```

padStart
```javascript
let num = 5;
let res = ''.padStart(num, '0');
console.log(res)
```

Array.from()
```javascript
let num = 5;
let res = Array.from({ length: num }, () => '0').join('');
console.log(res)
```

## Посчитать сумму элементов вложенного массива
reduce для двумерного массива (рекомендуемый)
```javascript
let array = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
]

let sum = array.reduce((acc, subArray) => 
  acc + subArray.reduce(subAcc, num) => subAcc + num, 0),
  0
);
```

for...of
```javascript
let array = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
]

let sum = 0;
for (const subArray of array) {
	for (const num of subArray) sum += num;
}

console.log(sum);
```

for
```javascript
let array = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
]

let sum = 0;
for (let i = 0; i < array.length; i++) {
  for (let j = 0; j < array[i].length; j++) {
    sum += array[i][j];
  }
}
```

flat + reduce (минус: промежуточный расплющенный массив -> больше расход памяти)
```javascript
let array = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
]

let sum = array.flat().reduce((acc, num) => acc + num, 0);
```

## Проверить, что каждая цифра нечётная
Моё решение
```javascript
const num = 1357;

const result = String(num).split('').every(i => i % 2 !== 0);

console.log(result);
```

Регулярное выражение
```javascript
const num = 1357;
const result = !/[02468]/.test(String(num));

console.log(result); // true, если нет чётных цифр
```