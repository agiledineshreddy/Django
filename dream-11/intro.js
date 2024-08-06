document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('.title').classList.add('show');
    setTimeout(function() {
        document.querySelector('.title').classList.remove('show');
        document.querySelector('.intro').classList.add('show');
    }, 2000); // 4000 milliseconds = 4 seconds
});

// Function to navigate to home.html
function gotologin() {
    location.href=("login.html ")
};
//login page
function mobile(){
document.querySelector(".mobile-logo").innerHTML="Mobile Number";
document.querySelector(".xicon").classList.add('sho');
}
document.querySelector("#xicon").addEventListener("click",function(){
    document.getElementById("input").value="";
   
    
});
// document.addEventListener("DOMContentLoaded", function() {
var checkb=document.getElementById("checkb");
var submitd=document.getElementById("submitd");
// checkb.onchange=function(){
//     submitd.disabled =!  this.checked;
// };
// });
// document.addEventListener("DOMContentLoaded", function() {
checkb.addEventListener("change",function(){
    if(this.checked){
        submitd.disabled = false;
        checkb.style.color = "green";
        submitd.style.backgroundColor = "green";
    }
    else{
        submitd.disabled=true;
        checkb.style.color = "";
        submitd.style.backgroundColor = "";
    }
});
// });