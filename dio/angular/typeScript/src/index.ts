// type heroi = {
//     name: string;
//     vulgo: string;
// };

// function printaObjeto(pessoa: heroi){
//     //console.log(pessoa);
// }

// printaObjeto({
//     name: "David Sousa",
//     vulgo: "Play",
// })

// function apiVersao(version: string){
//     return (target: any) => {
//         Object.assign(target.prototype, {__version: version, __nome: "David" });
//     }
// }


// @apiVersao("1.7")
// class Api{

// }

// const api = new Api();
// console.log(api.__version);

//decorators
//class decorator
function apiVersion(version: string) {
  return (target: any) => {
    Object.assign(target.prototype, { __version: version, __name: "David" });
  };
}

//attribute decorator
function minLength(length: number) {
  return (target: any, key: string) => {
    let _value = target[key];

    const getter = () => "[play]" + _value;
    const setter = (value: string) => {
      if (value.length < length) {
        throw new Error(`Tamanho menor do que ${length}`);
      } else {
        _value = value;
      }
    };

    Object.defineProperty(target, key, {
      get: getter,
      set: setter,
    });
  };
}

class Api {
  @minLength(10)
  name: string;

  constructor(name: string) {
    this.name = name;
  }
}

const api = new Api("David Sousa");
console.log(api.name);