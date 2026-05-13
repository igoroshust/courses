const button = document.querySelector('.button');
const number = document.querySelector('.number');


button.addEventListener('click', function(){
    number.value.textContent = number * 2;
});