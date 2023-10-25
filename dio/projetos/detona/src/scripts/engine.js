const state = {
    view: {
        squares: document.querySelectorAll(".square"),
        enemy: document.querySelector(".enemy"),
        timeLeft: document.querySelector("#time-left"),
        score: document.querySelector("#score"),
    },
    values: {
        timerId: null,
        gameVelocity: 100,
    }
}

function randomSquare(){
    
    state.view.squares.forEach((square) =>{
        square.classList.remove("enemy");
    });
    
    let randomNumber = Math.floor(Math.random()* 9);
    let randomSquare = state.view.squares[randomNumber];
    randomSquare.classList.add("enemy");
}
function moveEnemy(){
    
    state.values.timerId = setInterval(randomSquare,state.values.gameVelocity);
}
function addListinerHitBox(){
    state.view.squares.forEach((square) =>{
        /*if(square.id === )*/
    });
}

function main(){
    moveEnemy();
}

main();