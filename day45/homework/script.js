document.getElementById('score1')
document.getElementById('score2')

player_1 = 0
player_2 = 0

let dice = {
  roll: function () {
    var randomNumber = Math.floor(Math.random() * this.sides) + 1;
    document.getElementById('myp')
    return randomNumber;
  }
}

  

  
  