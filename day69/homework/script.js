
let number = 0

document.getElementById("btn").onclick = function(){
    number += 1;
    document.getElementById("text").innerHTML = number;
}


const div = document.getElementById("div")
let text = document.getElementById("text")

function change (event){
    document.getElementById("div").style.background = "rgba(116, 0, 0, 0.822)";
    document.getElementById("text").style.color = "black"
}


div.addEventListener("click", change)