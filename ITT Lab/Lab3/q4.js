function permute(){

    var test = "hello"
    var val=document.getElementById("word").value;
    const str = val.split("");
    const arr = [];
    
    
    for(let i=0;i<str.length-2;i++){
        
      for(let j = i+1 ;j < str.length-1; j++)
        {
        for(let k = j+1; k< str.length; k++)
            {
            const word = str[i]+str[j]+str[k];
            console.log(word);
            arr.push(word);
            arr.push(str[i]+str[k]+str[j]);
            arr.push(str[j]+str[i]+str[k]);
            arr.push(str[j]+str[k]+str[i]);
            arr.push(str[k]+str[i]+str[j]);
            arr.push(str[k]+str[j]+str[i]);
            }
        }
    }
    var op = "";
    for(i=0;i<arr.length;i++){
            op = op + arr[i]+" ";
        
       
    }
    
    document.getElementById("output").value = op;
}