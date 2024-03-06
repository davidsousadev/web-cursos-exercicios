### Instalação VITE + REACT
```sh
    npm create vite@latest my-vue-app -- --template react
```
#### Trocar de versão NODEJS
```sh
    export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
```
#### Start project
```sh
    cd app-react-vite
    npm install
    npm run dev
```

##### Production project
```sh
    npm run build
```