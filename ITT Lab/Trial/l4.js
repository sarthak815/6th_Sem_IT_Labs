function execute(){
    let n = document.getElementById("input").value;
    fibbo(n);
    squares(n);
}

function fibbo(n){
    let op = "";
    let prevn = 0;
    let currn = 1;
    let temp = 0;
    let text = document.getElementById("output");
    for(let i=0;i<n;i++){
        console.log("Curr-->"+currn);
        console.log("Prev-->" + prevn);
        op += currn+" ";
        temp = currn;
        currn = prevn+currn;
        prevn=temp;
        
    }
    text.innerHTML = op;
}

function squares(n){
    let sq = 0;
    let table = document.getElementById("tableop");
    for(let i=1;i<=n;i++){
        console.log("i->"+i+" n->"+n);
        let row = table.insertRow(-1);
        row.insertCell(-1).innerHTML = i;
        row.insertCell(-1).innerHTML = Math.pow(i,2);
    }

}