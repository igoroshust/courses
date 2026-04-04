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