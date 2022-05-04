function execute(){
    let table = document.getElementById("output");
    let data = JSON.parse(localStorage.getItem("clr"));
    console.log(data);
    // console.log(data.Name);
    // for(let i=0;i<Object.keys(data).length;i++){
    //     let row = table.insertRow(-1);
    //     row.insertCell(-1).innerHTML = data.emplyees[i].Name;
    //     // row.insertCell(-1).innerHTML = data[i].Gender;
    //     // row.insertCell(-1).innerHTML = data[i].Homeworld;
    //     // row.insertCell(-1).innerHTML = data[i].Born;
    //     // row.insertCell(-1).innerHTML = data[i].Jedi;
    // }
}