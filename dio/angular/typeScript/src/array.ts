function concatenaArray<T>(...itens: T[]): T[]{
    return new Array().concat(...itens);
}

const numeros = concatenaArray<number[]>([55,500],[10]);
const letras = concatenaArray<string[]>(['Uma',' frase',' qualquer','.',' '],["Outra"]);

console.log(numeros);
console.log(letras);
