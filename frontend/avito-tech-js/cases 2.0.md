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

## Посчитать сумму элементов вложенного массива

Моё решение
```javascript
let arr = [
	[
		[11, 12, 13],
		[14, 15, 16],
		[17, 17, 19],
	],
	[
		[21, 22, 23],
		[24, 25, 26],
		[27, 27, 29],
	],
	[
		[31, 32, 33],
		[34, 35, 36],
		[37, 37, 39],
	],
];

const result = arr.flat(2).reduce((acc, item) => acc + item, 0);
// можно flat(Infinity) - гарантировано развернёт массив любой вложенности

console.log(result);
```

Вложенные циклы
```javascript
let arr = [
	[
		[11, 12, 13],
		[14, 15, 16],
		[17, 17, 19],
	],
	[
		[21, 22, 23],
		[24, 25, 26],
		[27, 27, 29],
	],
	[
		[31, 32, 33],
		[34, 35, 36],
		[37, 37, 39],
	],
];
let sum = 0;

for (let i = 0; i < arr.length; i++) {
  for (let j = 0; j < arr[i].length; j++) {
    for (let k = 0; k < arr[i][j].length; k++) {
      sum += arr[i][j][k];
    }
  }
}

console.log(sum); // 672
```

Рекурсивная функция
```javascript
function sumNestedArray(array) {
  return array.reduce((acc, item) => {
    if (Array.isArray(item)) {
      return acc + sumNestedArray(item);
    } else {
      return acc + item;
    }
  }, 0);
}
```

forEach
```javascript

let arr = [
	[
		[11, 12, 13],
		[14, 15, 16],
		[17, 17, 19],
	],
	[
		[21, 22, 23],
		[24, 25, 26],
		[27, 27, 29],
	],
	[
		[31, 32, 33],
		[34, 35, 36],
		[37, 37, 39],
	],
];
let sum = 0;

arr.forEach(block => {
    console.log('block :>> ', block); // [ [ 11, 12, 13 ], [ 14, 15, 16 ], [ 17, 17, 19 ] ]
  block.forEach(row => {
    console.log('row :>> ', row); // [ 11, 12, 13 ]
    row.forEach(num => {
        console.log('num :>> ', num); // 11 (потом 12, 13)
      sum += num;
    });
  });
});

console.log(sum); // 672
```

## Поменять элементы массива местами

for
```javascript
let arr = [1, 2, 3, 4, 5, 6, 7, 8];

for (let i = 0; i < arr.length - 1; i += 2) {
    [arr[i], arr[i+1]] = [arr[i+1], arr[i]];
}

console.log(arr);
```

Моё решение
```javascript
let arr = [1, 2, 3, 4, 5, 6, 7, 8];

arr.forEach((item, index) => index % 2 !== 0 ? [ arr[index-1], arr[index] ] = [ item, arr[index-1] ] : '' );

console.log(arr);
```

## Найти сумму элементов объекта

Моё решение
```javascript
let obj = {
	1: {
		1: 11,
		2: 12,
		3: 13,
	},
	2: {
		1: 21,
		2: 22,
		3: 23,
	},
	3: {
		1: 24,
		2: 25,
		3: 26,
	},
}

let sum = 0;

for (let row of Object.values(obj)) {
    for (let item of Object.values(row)) {
        sum += item;
    }
}

console.log(sum);
```

Функциональный стиль
```javascript
function sumNestedObject(obj) {
    let sum = 0;
    for (const row of Object.values(obj)) {
        for (const item of Object.values(row)) {
            sum += Number(item);
        }
    }
    return sum;
}
```

reduce
```javascript
const sum = Object.values(obj).flatMap(Object.values).reduce((sum, num) => sum + num, 0);

// Object.values(obj).flatMap(Object.values) // [11, 12, 13, 21, 22, 23, 24, 25, 26]

// Сначала к каждому элементу применяется Object.values, получаем массив [11,12,13]

// Затем примеяем flat(), расщипляя массивы на 1 уровень: [11, 12, 13, 21, 22, 23, 24, 25, 26]


console.log('🔹 1. Object.values(obj):');
console.log(Object.values(obj));

console.log('\n🔹 2. .map(Object.values):');
// Элемент 1: {1:11,2:12,3:13} → Object.values() → [11,12,13]
console.log(Object.values(obj).map(Object.values)); // [ [ 11, 12, 13 ], [ 21, 22, 23 ], [ 24, 25, 26 ] ]

console.log('\n🔹 3. .flatMap(Object.values):'); 
console.log(Object.values(obj).flatMap(Object.values)); // [11, 12, 13, 21, 22, 23, 24, 25, 26]

console.log('\n🔹 4. Итоговая сумма:');
console.log(Object.values(obj).flatMap(Object.values).reduce((a,b)=>a+b,0));
```

Деструктуризация
```javascript
let sum = 0;
for (let [, row] of Object.entries(obj)) {
  for (let [, item] of Object.entries(row)) {
    sum += item;
  }
}
```


## Найти сумму элементов объекта

Вложенный flatMap
```javascript
let obj = {
	1: {
		1: {
			1: 111,
			2: 112,
			3: 113,
		},
		2: {
			1: 121,
			2: 122,
			3: 123,
		},
	},
	2: {
		1: {
			1: 211,
			2: 212,
			3: 213,
		},
		2: {
			1: 221,
			2: 222,
			3: 223,
		},
	},
	3: {
		1: {
			1: 311,
			2: 312,
			3: 313,
		},
		2: {
			1: 321,
			2: 322,
			3: 323,
		},
	},
}

let sum = Object.values(obj)
    .flatMap(Object.values)
    .flatMap(Object.values)  // ← добавьте еще один flatMap!
    .reduce((sum, num) => sum + num, 0);

console.log(sum); // 2346
```

Моё решение
```javascript
let sum2 = 0;

for (let firstLevelKeys of Object.values(obj)) {
    for (let secondLevelKeys of Object.values(firstLevelKeys)) {
        for (let item of Object.values(secondLevelKeys)) {
            console.log('item :>> ', item);
            sum2 += item;
        }
    }
}

console.log(sum2);
```

Генератор
```javascript
function* flatten(obj) {
    for (const value of Object.values(obj)) {
        if (typeof value === 'number') yield value;
        else yield* flatten(value);
    }
}

const sum = [...flatten(obj)].reduce((a, b) => a + b, 0);
```

## Записать значения в массив посимвольно

Моё решение
```javascript
let arr = [123, 456, 789];

const one = arr.join('').split('').map(Number);
const two = array => {
    let newArr = '';
    for (let i = 0; i < array.length; i++) {
        newArr += array[i];
    }
    return newArr.split('').map(Number);
}

const result = String();

console.log(two(arr));
```

Array.from() + String()
```javascript
let arr = [123, 456, 789];

const result = Array.from(arr.join(''), Number);
console.log(result);

// Array.from(string, mapFn) создаёт массив из строки и сразу применяет функцию Number К каждому символу
```

spread + map()
```javascript
let arr = [123, 456, 789];
const result = [...arr.join('')].map(Number);
```

for
```javascript

let arr = [123, 456, 789];
const result = [];

for (const num of arr) {
  const digits = String(num).split('').map(Number);
  result.push(...digits);
}
```

## Пример thisArg в Array.from()

```javascript
const context = {
  multiplier: 2,
  transform(value) {
    return value * this.multiplier;
  }
};

const result = Array.from([1, 2, 3, 4], function(value) {
  return this.transform(value);
}, context);

console.log(result); // [2, 4, 6, 8]
```

## Найти сумму элементов структуры 

Рекомендация для production (без промежуточных массивов)
```javascript
let data = [
	{
		1: 11,
		2: 12,
		3: 13,
	},
	{
		1: 21,
		2: 22,
		3: 23,
	},
	{
		1: 24,
		2: 25,
		3: 26,
	},
];

const sumObjectValues = arr => arr.reduce((sum, obj) => sum + Object.values(obj).reduce((a, b) => a + b, 0), 0);

const result = sumObjectValues(data);
```

Проверка работы
```javascript
console.time('ваш');
data.flatMap(Object.values).reduce((s,n)=>s+n,0);
console.timeEnd('ваш');     // ~12ms

console.time('мой');  
data.reduce((s,obj)=>s+Object.values(obj).reduce((a,b)=>a+b,0),0);
console.timeEnd('мой');     // ~8ms
```

Функциональный стиль
```javascript
let data = [
	{
		1: 11,
		2: 12,
		3: 13,
	},
	{
		1: 21,
		2: 22,
		3: 23,
	},
	{
		1: 24,
		2: 25,
		3: 26,
	},
];
```

Моё решение (минус - создаёт промежуточный массив)
```javascript
let data = [
	{
		1: 11,
		2: 12,
		3: 13,
	},
	{
		1: 21,
		2: 22,
		3: 23,
	},
	{
		1: 24,
		2: 25,
		3: 26,
	},
];

const result = data.flatMap(Object.values).reduce((sum, num) => sum + num, 0);

console.log(result);

/* Более читаемый вариант */
// const result = data.reduce((totalSum, item) => {
//   const itemSum = Object.values(item).reduce((sum, num) => sum + num, 0);
//   return totalSum + itemSum;
// }, 0);

// console.log(result); // 177
```

Функциональный стиль
```javascript
let data = [
	{
		1: 11,
		2: 12,
		3: 13,
	},
	{
		1: 21,
		2: 22,
		3: 23,
	},
	{
		1: 24,
		2: 25,
		3: 26,
	},
];

const sumBy = (arr, fn) => arr.reduce((sum, item) => sum + fn(item), 0);

const result = sumBy(data, obj => Object.values(obj).reduce((a, b) => a + b, 0));

console.log(result);
```

lodash (библиотека для работы с данными)
```javascript
npm install lodash

const result = _.sum(_.flatMap(data, _.values));
```

## Тестирование (для точности)
```javascript
// Тестируем 3 раза для точности
function benchmark(fn, name) {
  let total = 0;
  for(let i=0; i<3; i++) {
    console.time(name);
    fn();
    console.timeEnd(name);
  }
}

benchmark(() => data.flatMap(Object.values).reduce((s,n)=>s+n,0), 'flatMap');
```

## Отсортировать слова в строке в алфавитном порядке
Моё решение
```javascript
let string = 'Съешь этих мягких французских булок и выпей же чаю';

const result = string.toLowerCase().split(' ').sort((a, b) => a.localeCompare(b, 'ru')).join(' ');

console.log(result);
```

## Найти сумму элементов структуры

Моё решение
```javascript
let data = [
    {
        1: [1, 2, 3],
        2: [1, 2, 3],
        3: [1, 2, 3],
    },
    {
        1: [1, 2, 3],
        2: [1, 2, 3],
        3: [1, 2, 3],
    },
    {
        1: [1, 2, 3],
        2: [1, 2, 3],
        3: [1, 2, 3],
    },
];


const result = data.reduce((sum, row) => sum+Object.values(row).flat(Infinity).reduce((s, i) => s + i, 0), 0);

console.log(result);
```

Компактный flatMap + reduce
```javascript

const result = data.flatMap(row => Object.values(row).flat()).reduce((sum, num) => sum + num, 0);

```

# Сформировать массив с помощью циклов [[1, 2, 3], [4, 5, 6], [7, 8, 9],]

Оптимальный вариант
```javascript
const createRangeArray = (value, rows, elements=3) => {
    const resultArray = [];
    let current = value;

    for (let i = 0; i < rows; i++) {
        const start = current;
        const row = [];
        
        // Создаём строку за один проход
        for (let j = 0; j < elements; j++) {
            row[j] = start + j;
        }
        resultArray[i] = row;
        console.log('current :>> ', current); // 1 4 7
        current += elements;
    }

    return resultArray;
}

console.log(
    createRangeArray(1, 3)
);
```

Моё решение
```javascript
const createRangeArray = (value, rows, elements=3) => {
    let resultArray = [];
    let acc = value;
    for (let i = 0; i < rows; i++) {
        let parts = [];
		for (let j = 0; j < elements; j++) {
			parts.push(acc);
			acc++;
		}
        resultArray.push(parts);
    }
    return resultArray;
}

const result = createRangeArray(1, 3);

console.log(result);
```

Array.from() + flatMap()
```javascript
const createRangeArray = (start, rows, elements = 3) => {
    return Array.from({ length: rows }, (_, rowIndex) =>
        Array.from({ length: elements }, (_, colIndex) =>
            start + rowIndex * elements + colIndex
        )
    );
};

console.log(createRangeArray(1, 3));
```

# Вернуть max и min
spread
```javascript
const defineMinMaxValue = array => { 
	return { 
		max: Math.max(...array),
		min: Math.min(...array)
	};
};

console.log(defineMinMaxValue([1, 2, 3])); 
// { max: 3, min: 1 }
```

apply
```javascript
const defineMinMaxValue = array => {
	return {
		max: Math.max.apply(null, array),
		min: Math.min.apply(null, array)
	};
};

console.log(defineMinMaxValue([1, 2, 3]));
// { max: 3, min: 1 }
```