let number = 123789;

const getEvenDigits = num => {
    let result = '';
    for (let digit of String(Math.abs(num))) {
        if (digit % 2 === 0) result += digit;
    }
    return result;
}

console.log('getEvenDigits(number) :>> ', getEvenDigits(number));