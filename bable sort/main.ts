let numbers = [9, 5, 4, 1, 7, 94, 513, 574, -1, -200, 0];

for (let i = 0; i < numbers.length; i++) {
    
    for (let j = 0; j < numbers.length - i - 1; j++) {
        
        if (numbers[j] > numbers[j + 1]) {
            let temp = numbers[j];
            numbers[j] = numbers[j + 1];
            numbers[j + 1] = temp;
        }
        
    }
}

console.log(numbers);
