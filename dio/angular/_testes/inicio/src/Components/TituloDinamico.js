class TituloDinamico extends HTMLElement{
    constructor(){
        super();
        const shadow = this.attachShadow({mode: "open"});
        const componenteRoot = document.createElement("h1");
        // componenteRoot.textContent = ('David');
        componenteRoot.textContent = this.getAttribute("titulo");
        // shadow.innerHTML = componenteRoot.textContent;

        const style = document.createElement("style");
        style.textContent = `
            h1{
                color: red;

            }
        `
        shadow.appendChild(componenteRoot);
        shadow.appendChild(style);

    }
}

customElements.define('titulo-dinamico', TituloDinamico);//a teg que vai ser criada precisa de - para ser reconhecida