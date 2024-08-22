Crie um Projeto Node.js e Instale Dependências

Se ainda não fez isso, você precisa iniciar um projeto Node.js e instalar as dependências necessárias para rodar testes. Vou usar npm como exemplo:

# Inicialize um novo projeto Node.js (se ainda não tiver um package.json)
```
npm init -y
```
# Instale o Jest como dependência de desenvolvimento
```
npm install --save-dev jest
```
Se você preferir usar yarn, o comando seria:

```
yarn init -y
yarn add --dev jest
```

# Configure o Jest

Configure o Jest

Adicione uma configuração básica do Jest ao seu package.json. Isso permite que o Jest encontre seus arquivos de teste e os execute:

No package.json, adicione uma seção "scripts" se ainda não existir:

"scripts": {
  "test": "jest"
}


# rodando todos os testes

`npm run test`

# rodando teste de arquivos especificos

`npm test path`