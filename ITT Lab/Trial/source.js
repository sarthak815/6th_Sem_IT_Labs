let word;
function convert(){
    word = document.getElementById("word").value;
    let words = word.split(' ');
    for(let j=0;j<words.length;j++){
        let new_word = words[j].slice(1,) + word[j][0]+"ay";
        document.getElementById("output")
    .insertAdjacentText("afterbegin", new_word+"\n");
    }
    //let new_word = word.slice(1,) + word[0]+"ay";
    
}