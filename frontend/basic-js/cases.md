## Дана некоторая строка. Переберите и выведите в консоль по очереди все символы с конца строки.

```javascript
const string = 'абырвалг';

for (let i = string.length - 1; i >= 0; i--) {
    console.log(string[i]);
}
```