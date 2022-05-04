function generate(){
    let table = document.getElementById("output");
  
    for(let i=1;i<11;i++){
        let row = table.insertRow(-1);
        let square = Math.pow(i,2);
        let cube = Math.pow(i,3);
        row.insertCell(-1).innerHTML = i.toString();
        row.insertCell(-1).innerHTML = square.toString();
        row.insertCell(-1).innerHTML = cube.toString();
        
    }
}