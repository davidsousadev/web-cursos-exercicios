const emojis = [
    "🐱",
    "🐱",
    "🦝",
    "🦝",
    "🦊",
    "🦊",
    "🐶",
    "🐶",
    "🐵",
    "🐵",
    "🦁",
    "🦁",
    "🐯",
    "🐯",
    "🐮",
    "🐮",
];
let openCards = [];


let randonEmojis = emojis.sort(()=>(Math.random() > 0.5 ? 2 : -1));

for (let i = 0; i < emojis.length; i++){
    let box = document.createElement("div");
    box.className = "item";
    box.innerHTML = randonEmojis[i];
    box.onclick = handclick;
    document.querySelector(".game").appendChild(box);
}

function handclick(){
    if(openCards.length < 2){
        this.classList.add("boxOpen");
        openCards.push(this);/**guarda no vetor*/
    }
    if (openCards.length == 2) {
        setTimeout(checkMatch, 500);
    }
}

function checkMatch(){
    
}