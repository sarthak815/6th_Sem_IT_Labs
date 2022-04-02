
var i;
function modify(){
    text = document.getElementById("palceholder").textContent;
    var words = String.split(" ");
    const n = words.length;
    var newls = new Array(n);
    for(i=0;i<n;i++){
        text = words[i];
        const len = text.length;
        text = text.substring(1,n)+text[0]+"ay";
        newls[i] = text;
    }
    var textn = "kidjasifi" 
    //= newls.join(" ");
    document.getElementById("placeholder").textContent = textn;
}

function printLatinWord(token){
    if (token === " ") return token; 
    rotatedToken = token.substring(1) + token.charAt(0);
    latinToken = rotatedToken + "ay";
    return latinToken;
}

function convert(initialString){
    var words = initialString.split(" ");
    const n = words.length;
    var newls = new Array(n);
    for(i=0;i<n;i++){
        text = words[i];
        const len = text.length;
        text = text.substring(1,len)+text[0]+"ay";
        newls[i] = text;
    }
    var finalString = newls.join(" ");
    return finalString;
}

function updateStatus(){
    var text = document.getElementById("inputText").value;
    var converted = convert(text);
    var d1 = document.getElementById("output");
    d1.insertAdjacentHTML('afterbegin', '<p>' + converted + '</p>');
    console.log(d1.innerHTML);
}