"use strict";
function concatenaArray(...itens) {
    return new Array().concat(...itens);
}
const numeros = concatenaArray([55, 500], [10]);
const letras = concatenaArray(['Uma', ' frase', ' qualquer', '.', ' '], ["Outra"]);
console.log(numeros);
console.log(letras);
console.log(letras);
