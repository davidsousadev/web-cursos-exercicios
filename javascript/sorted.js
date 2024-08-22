
/* function getSortedEvenNumbers(numbers){
    return numbers
} */

  /* */
function getSortedEvenNumbers(numbers) {
    let evenNumbers = [];

    // Filtra números pares
    for (let i = 0; i < numbers.length; i++) {
        if (numbers[i] % 2 === 0) {
            evenNumbers.push(numbers[i]);
        }
    }

    // Ordena números pares
    for (let i = 0; i < evenNumbers.length; i++) {
        for (let j = i + 1; j < evenNumbers.length; j++) {
            if (evenNumbers[i] > evenNumbers[j]) {
                let temp = evenNumbers[i];
                evenNumbers[i] = evenNumbers[j];
                evenNumbers[j] = temp;
            }
        }
    }

    return evenNumbers;
}

/* 
// Código refatorado 1
function getSortedEvenNumbers(numbers){
    return numbers.sort((a, b) => a - b);
}
*/


// Código refatorado 2
// function getSortedEvenNumbers(numbers){
//     return numbers
//         .filter(num => num % 2 === 0)
//         .sort((a, b) => a - b);
// }



module.exports = { getSortedEvenNumbers };
