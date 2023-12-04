function ExibirMome(target: any): void{
    console.log(target);
}

@ExibirMome
class People{}

@ExibirMome
class aluno{}

// function apiVersao(version: string){
//     return (target: any) => {
//         Object.assign(target.prototype, {__version: version, __nome: "David" });
//     }
// }


// @apiVersao("1.77")
// class Api{

// }

// const api = new Api();
// console.log(api.__version);