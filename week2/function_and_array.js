function max(numbers) {
    if (numbers.length !== 0) {
        let max_number = numbers[0]
        for (let number of numbers) {
            if (number > max_number) {
                max_number = number;
            }
        } return `${max_number}`;
    } else {
        return null;
    }
};



function findPosition(numbers, target) {
    for (let i = 0; i < numbers.length; i++) {
        if (numbers[i] === target) {
            return `${i}`
        }
    } return '-1'
}

console.log(max([1, 2, 4, 5]));
console.log(max([5, 2, 7, 1, 6]));

console.log(findPosition([5, 2, 7, 1, 6], 5))
console.log(findPosition([5, 2, 7, 1, 6], 7))
console.log(findPosition([5, 2, 7, 7, 7, 1, 6], 7))
console.log(findPosition([5, 2, 7, 1, 6], 8))

