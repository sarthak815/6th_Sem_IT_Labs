var text_small = "TEXT-SHRINKING";
var text_large = "TEXT-GROWING";
var increment = 1;
var text = "";
var change = true;
var color = "red";
var fontSize = 5;
function modify(text, size,color){
    document.getElementById("placeholder_text").innerHTML = text;
    document.getElementById("placeholder_text").style.color = color;
    document.getElementById("placeholder_text").style.fontSize = size;
}

function update(){
    if(increment==5&& change==true){
        change=false;
    }
    if(increment==0&&change==false){
        change=true;
    }
    if(increment<5&&change==true){
        color = "blue";
        modify(text_large, (increment+20).toString()+"pt", color);
        increment+=1;
  
    }
    if(increment>0&&change==false){
        color = "red";
        modify(text_small, (increment+20).toString()+"pt", color);
        increment-=1;
    
    }
}

setInterval(update,500);