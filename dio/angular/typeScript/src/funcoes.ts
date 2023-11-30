//import * as readlineSync from 'readline-sync';
function soma(x: number, y: number): number{
    return x + y;
}

function saudacao(nome:string): string{
    return `Ola ${nome}`;
}

function telefone(fone: number | string){
    return fone;
}

async function database(id: number): Promise<string>{
    return "David Sousa"
}

//let nome = readlineSync.question('Digite algo: ');
let somar: number = soma(3, 7);
let nome = saudacao("David");
let phone = telefone(15482643);
let nomebd = database(10);


console.log(nome);
console.log(somar);