const form = document.getElementById("form");
const button = document.getElementById("done")

form.addEventListener("done" , function(my)){

    const Node = document.createElement("p")
    const textNode = document.createTextNode(elemets.name.value)

    textNode.appendChild(Node)
    Node.appendChild(textNode)
}