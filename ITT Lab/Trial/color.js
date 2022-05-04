function execute(color){
    // console.log(color);
    // document.getElementById("body").style.backgroundColor=color;
    // alert(color+" set!");
}
$(document).ready( function(){
    $("#blue").mouseenter(function(){
        console.log("ok");
        $("body").css("background-color","blue");
    });
    $("#blue").mouseleave(function(){
        console.log("ok");
        $("body").css("background-color","green");
    });
});