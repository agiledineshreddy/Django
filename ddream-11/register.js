
//login page
function mobile(){
    document.querySelector(".mobile-logo").innerHTML="Mobile Number";
    document.querySelector(".xicon").classList.add('sho');
    }
    document.querySelector("#xicon").addEventListener("click",function(){
        document.getElementById("input1").value="";
        document.getElementById("input2").value="";
        
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