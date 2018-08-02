

function openNav() {
    document.getElementById("mySidenav").style.width = "200px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0px";
}

$(".menu-icon").click(function(){
    $(".menu-icon").hide();
})

$(".closebtn").click(function(){
    $(".menu-icon").show();
})