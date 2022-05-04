let data = {

    "item1":{
        "name":"sam",
        "branch":"IT"
    },

    "item2":{
        "name":"Tom",
        "branch":"CCE"
    }
}

function execute(){
    // let obj = JSON.parse(data);
    let div = document.getElementById("div1");
    div.insertAdjacentHTML("afterend", data.item1.name);
    div.insertAdjacentHTML("afterend", data.item1.branch);
}