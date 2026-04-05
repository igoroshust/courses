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