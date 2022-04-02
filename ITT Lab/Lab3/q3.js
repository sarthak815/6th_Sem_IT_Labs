function split(){
    var text = document.getElementById("extract").value;
    var ccode = country(text);
    var phone = remnumber(text);
    document.getElementById("ccode").value = ccode;
    document.getElementById("phone").value = phone;
}

function country(number){
    var country = number.substr(0,3);
    return country;
}

function remnumber(number){
    var phone = number.substr(3,);
    return phone;
}