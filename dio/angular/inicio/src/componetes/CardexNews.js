class CardNews extends HTMLElement{
    constructor(){
        super();
        const shadow =  this.attachShadow({mode: "open"});
        shadow.innerHTML = this.getAttribute("titulo");
    }
}

customElements.define('card-news', CardNews);