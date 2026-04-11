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