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