type robo = {
    readonly id: number;
    nome: string;
};

interface robo2{
    id: number | string;
    nome: string;
};

const bot: robo = {
    id: 1,
    nome: "GPT"
};

console.log(bot);