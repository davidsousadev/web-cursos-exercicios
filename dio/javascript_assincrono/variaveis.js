var var3 = function var3() {
    console.log("Var3");
    var var5 = "Var5";
}
var var6 = 0
if (var6==0){
    var6 = 5
}
function var4(){
    console.log("Var4");
}
var var1 = 10;
var var2 = "Texte";

console.log(var1 + var2);
var3();
var4();
//console.log(var5);//erro, pois o VAR não vaza de função
console.log(var6);//vazou de estrutura de decisão

if(true){
    let var7 = 10
}

//console.log(var7);//erro, LET não vaza de blocos

const var8 = 3.14

console.log(var8)
/*
var8 = ++

console.log(var8);//não pode ser alterado uma CONST
*/

var $var9 = 0
let $var10 = 0
const $var11 = 0

var _var12 = 0
const VAR13 = 0