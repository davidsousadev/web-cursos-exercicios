//import * as readlineSync from 'readline-sync';
function soma(x: number, y: number): number{
    return x + y;
}

let somar: number = soma(3, 7);

function saudacao(nome:string): string{
    return `Ola ${nome}`;
}

//let nome = readlineSync.question('Digite algo: ');
let nome = saudacao("David");
console.log(nome);
console.log(somar);