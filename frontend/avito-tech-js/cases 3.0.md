# Даны два инпута, абзац и кнопка. В инпуты вводятся числа. По нажатию на кнопку выведите в абзац сумму этих чисел.
Моё решение
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JS Bin</title>
</head>
<body>
  
  <!--
  Даны два инпута, абзац и кнопка. 
  В инпуты вводятся числа. 
  По нажатию на кнопку выведите в абзац сумму этих чисел.

  -->
  
  <form action="/" method="get" id="taskForm" name="task">
    <input type="number" id="taskForm__firstNumber" name="firstNumber" value="" placeholder="Введите первое число" >
    <input type="number" id="taskForm__secondNumber" name="secondNumber" value="" placeholder="Введите второе число">
    <input type="submit" id="taskForm__btn" value="Расчитать">
  </form>
  
  <div id="taskResult" style="display: none;">
    <h4 id="taskResult__heading">Результат вычислений:</h4>
    <p class="taskResult__paragraph"></p>
  </div>

</body>
</html>
```

```javascript
const firstNumber = document.getElementById('taskForm__firstNumber');
const secondNumber = document.getElementById('taskForm__secondNumber');
const button = document.getElementById('taskForm__btn');
const contentBlock = document.getElementById('taskResult');
const paragraph = document.querySelector('.taskResult__paragraph');


button.addEventListener('click', function(e){
  const sum = +firstNumber.value + +secondNumber.value;
  paragraph.innerText = sum;
  
  
  contentBlock.style.display = 'block';
});
```


Решение ИИ
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Калькулятор</title>
  <style>
    /* Тот же CSS что и раньше */
  </style>
</head>
<body>
  <div class="form-container">
    <form id="calcForm">
      <input type="number" id="firstNumber" placeholder="Первое число" required>
      <input type="number" id="secondNumber" placeholder="Второе число" required>
      <button type="submit" id="calcBtn">Сумма</button>
    </form>
    <div id="result" class="result" style="display: none;">
      <p id="resultText">0</p>
    </div>
  </div>

</body>
</html>
```

```javascript
document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('calcForm');
  const firstInput = document.getElementById('firstNumber');
  const secondInput = document.getElementById('secondNumber');
  const button = document.getElementById('calcBtn');
  const result = document.getElementById('result');
  const resultText = document.getElementById('resultText');

  form.addEventListener('submit', function(e) {
    e.preventDefault();
    
    const num1 = Number(firstInput.value);
    const num2 = Number(secondInput.value);
    
    if (isNaN(num1) || isNaN(num2)) {
      resultText.textContent = 'Ошибка: введите числа!';
      result.className = 'result error';
    } else {
      resultText.textContent = `Сумма: ${num1 + num2}`;
      result.className = 'result';
    }
    
    result.style.display = 'block';
    result.scrollIntoView({ behavior: 'smooth' });
  });
});
```

Расширенный пример ИИ
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Калькулятор суммы</title>
  <style>
    .form-container {
      max-width: 400px;
      margin: 20px auto;
      padding: 20px;
      font-family: Arial, sans-serif;
    }
    .form-group {
      margin-bottom: 15px;
    }
    input[type="number"] {
      width: 100%;
      padding: 10px;
      font-size: 16px;
      border: 1px solid #ddd;
      border-radius: 4px;
      box-sizing: border-box;
    }
    button {
      width: 100%;
      padding: 12px;
      background: #007bff;
      color: white;
      border: none;
      border-radius: 4px;
      font-size: 16px;
      cursor: pointer;
    }
    button:hover {
      background: #0056b3;
    }
    button:disabled {
      background: #ccc;
      cursor: not-allowed;
    }
    .result {
      margin-top: 20px;
      padding: 15px;
      background: #f8f9fa;
      border-radius: 4px;
      border-left: 4px solid #007bff;
      display: none;
    }
    .error {
      background: #f8d7da;
      border-left-color: #dc3545;
      color: #721c24;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <form id="calcForm">
      <div class="form-group">
        <input 
          type="number" 
          id="firstNumber" 
          name="firstNumber" 
          placeholder="Введите первое число"
          step="any" <!-- дробные числа -->
          required
        >
      </div>
      <div class="form-group">
        <input 
          type="number" 
          id="secondNumber" 
          name="secondNumber" 
          placeholder="Введите второе число"
          step="any"
          required
        >
      </div>
      <button type="submit" id="calcBtn">Рассчитать сумму</button>
    </form>
    
    <div id="result" class="result">
      <h4>Результат:</h4>
      <p id="resultText">0</p>
    </div>
  </div>
</body>
</html>
```

```javascript
class Calculator {
  constructor() {
    this.form = document.getElementById('calcForm');
    this.firstInput = document.getElementById('firstNumber');
    this.secondInput = document.getElementById('secondNumber');
    this.button = document.getElementById('calcBtn');
    this.resultDiv = document.getElementById('result');
    this.resultText = document.getElementById('resultText');
    
    this.init();
  }
  
  init() {
    this.form.addEventListener('submit', (e) => this.handleSubmit(e));
    
    // Валидация в реальном времени
    this.firstInput.addEventListener('input', () => this.toggleButton());
    this.secondInput.addEventListener('input', () => this.toggleButton());
  }
  
  handleSubmit(e) {
    e.preventDefault(); // Предотвращаем перезагрузку страницы
    
    const num1 = this.parseNumber(this.firstInput.value);
    const num2 = this.parseNumber(this.secondInput.value);
    
    if (num1 === null || num2 === null) {
      this.showError('Пожалуйста, введите корректные числа');
      return;
    }
    
    const sum = num1 + num2;
    this.showResult(`Сумма: <strong>${sum}</strong>`);
  }
  
  parseNumber(value) {
    const num = Number(value);
    return isNaN(num) ? null : num;
  }
  
  toggleButton() {
    const num1 = this.parseNumber(this.firstInput.value);
    const num2 = this.parseNumber(this.secondInput.value);
    const isValid = num1 !== null && num2 !== null;
    
    this.button.disabled = !isValid;
    this.button.textContent = isValid ? 'Рассчитать сумму' : 'Введите числа';
  }
  
  showResult(text) {
    this.resultText.innerHTML = text;
    this.result.className = 'result'; // Убираем класс ошибки
    this.result.style.display = 'block';
    this.result.scrollIntoView({ behavior: 'smooth' });
  }
  
  showError(text) {
    this.resultText.textContent = text;
    this.result.className = 'result error';
    this.result.style.display = 'block';
    this.result.scrollIntoView({ behavior: 'smooth' });
  }
}

// Запуск при загрузке страницы
document.addEventListener('DOMContentLoaded', () => {
  new Calculator();
});
```

Короткий с BEM
```html
<form class="calc" id="calcForm">
  <input class="calc__input" id="firstInput" name="first" type="number" step="any" required>
  <input class="calc__input" id="secondInput" name="second" type="number" step="any" required>
  <button class="calc__btn" type="submit">Сумма</button>
</form>
<div class="calc__result" id="result" style="display:none">
  <p class="calc__result-text" id="resultText">0</p>
</div>
```

```javascript
document.getElementById('calcForm').addEventListener('submit', e => {
  e.preventDefault();
  const a = Number(document.getElementById('firstInput').value);
  const b = Number(document.getElementById('secondInput').value);
  document.querySelector('.calc__result-text').textContent = 
    isNaN(a) || isNaN(b) ? 'Ошибка!' : `Сумма: ${a + b}`;
  document.querySelector('.calc__result').style.display = 'block';
});
```