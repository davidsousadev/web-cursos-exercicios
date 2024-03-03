numeros = 10;
numeros =  10.0;

string = "texto";
string = 'texto';

boleanos = true;
boleanos = false;

objetos = {
    chave: "Valor",
    nome: "david",
    idade: 27
}

array = [objetos["nome"], objetos.idade , "Ariely", 10];

console.log(typeof(numeros));
console.log(typeof(string));
console.log(typeof(boleanos));
console.log(typeof(objetos));
console.log(typeof(array));

console.log(objetos);
console.log(array);

console.log(array[1]+1);