fs = require('fs')
conversions = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}
var points = {"X":1,"Y":2,"Z":3}
var total = 0;
fs.readFile('./input.txt', 'utf8', function (err,data) {
  if (err) {
    return console.log(err);
  }
  for(var i=0; i<data.length/4; i++){
    row = i*4;
    letter1 = data[row]
    letter2 = data[row+2]
    total+=points[letter2]
    if(letter2 == conversions[letter1]){//tie
        total+=3
    } else {
        if(letter1=="A"){
            if(letter2=="Y"){
                total+=6
            }
        } else if(letter1=="B"){
            if(letter2=="Z"){
                total+=6
            }
        } else if(letter1=="C"){
            if(letter2=="X"){
                total+=6
            }
        }
    }
  }
  console.log(total)
});