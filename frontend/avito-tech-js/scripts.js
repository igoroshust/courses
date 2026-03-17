const arr = [1, 2, 3, 4, 5, 6];

const strangeFunction = array => {
    let evenNumbers=0;
    let oddNumbers=0;

    array.forEach(item => item % 2 === 0 ? evenNumbers += item : oddNumbers += item);
    return parseFloat((evenNumbers / oddNumbers).toFixed(2));
}

const result = strangeFunction(arr);
console.log(typeof result);